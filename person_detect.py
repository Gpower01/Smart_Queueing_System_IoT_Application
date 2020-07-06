
import numpy as np
import time
from openvino.inference_engine import IENetwork, IECore
import os
import cv2
import argparse
import sys

def check_supported_layers(engine, network, device):
    """
    When running OpenVINO, it is important to understand that not
    all layers are supported on each hardware type. So this function
    helps check the supported layers for the devices.
    :param Engine: IECore
    :param Network: IENetwork
    :param Device: Inference Device
    :return: True if all layers are supported, False if otherwise
    """
    supported_layers = engine.query_network(network, device_name=device)
    layers = network.layers.keys()
    
    all_supported_layers = True
    for l in layers:
        if l not in supported_layers:
            all_supported_layers = False
            print('Layer', l, 'is not supported on', device)
    if all_supported_layers:
        print('All layers are supported')
    return all_supported_layers 
    

class Queue:
    '''
    Class for dealing with queues
    '''
    def __init__(self):
        self.queues=[]

    def add_queue(self, points):
        self.queues.append(points)

    def get_queues(self, image):
        for q in self.queues:
            x_min, y_min, x_max, y_max=q
            frame=image[y_min:y_max, x_min:x_max]
            yield frame
    
    def check_coords(self, coords):
        d={k+1:0 for k in range(len(self.queues))}
        for coord in coords:
            for i, q in enumerate(self.queues):
                if coord[0]>q[0] and coord[2]<q[2]:
                    d[i+1]+=1
        return d


class PersonDetect:
    '''
    Class for the Person Detection Model.
    '''

    def __init__(self, model_name, device, threshold=0.60):
        self.model_weights=model_name+'.bin'
        self.model_structure=model_name+'.xml'
        self.device=device
        self.threshold=threshold

        try:
            self.model=IENetwork(self.model_structure, self.model_weights)
        except Exception as e:
            raise ValueError("Could not Initialise the network. Have you enterred the correct model path?")

        self.input_name=next(iter(self.model.inputs))
        self.input_shape=self.model.inputs[self.input_name].shape
        self.output_name=next(iter(self.model.outputs))
        self.output_shape=self.model.outputs[self.output_name].shape

    def load_model(self):
        '''
        TODO: This method needs to be completed by you
        '''
        core = IECore()
        self.network = core.load_network(network=self.model, device_name=self.device, num_requests=1)
        
        
    def predict(self, image):
        '''
        TODO: This method needs to be completed by you
        '''
        net_feed = self.preprocess_input(image)
        infer_request_matter = self.network.start_async(request_id=0, inputs=net_feed)
        if infer_request_matter.wait() == 0:
            net_output = infer_request_matter.outputs[self.output_name]
            detect = self.preprocess_outputs(net_output)
            return self.draw_outputs(detect, image)
    
    def draw_outputs(self, coords, image):
        '''
        TODO: This method needs to be completed by you
        '''
        width_w = image.shape[1]
        height_h = image.shape[0]
        detect = []
        for detect_box in coords:
            lane1 = (int(detect_box[0] * width_w), int(detect_box[1] * height_h))
            lane2 = (int(detect_box[2] * width_w), int(detect_box[3] * height_h))
            detect.append([lane1[0], lane1[1], lane2[0], lane2[1]])
            image = cv2.rectangle(image, lane1, lane2, (0, 0, 255), 3)
        return detect, image

    def preprocess_outputs(self, outputs):
        '''
        TODO: This method needs to be completed by you
        '''
        detect = []
        probs = outputs[0, 0, :, 2]
        for i, p in enumerate(probs):
            if p > self.threshold:
                detect_box = outputs[0, 0, i, 3:]
                detect.append(detect_box)
        return detect

    def preprocess_input(self, image):
        '''
        TODO: This method needs to be completed by you
        '''
        input_image_p = cv2.resize(image, (self.input_shape[3], self.input_shape[2]))
        input_image_p = input_image_p.transpose((2, 0, 1))
        input_image_p = input_image_p.reshape(1, *input_image_p.shape)
        return {self.input_name: input_image_p}


def main(args):
    model=args.model
    device=args.device
    video_file=args.video
    max_people=args.max_people
    threshold=args.threshold
    output_path=args.output_path

    start_model_load_time=time.time()
    pd= PersonDetect(model, device, threshold)
    pd.load_model()
    total_model_load_time = time.time() - start_model_load_time

    queue=Queue()
    
    try:
        queue_param=np.load(args.queue_param)
        for q in queue_param:
            queue.add_queue(q)
    except:
        print("error loading queue param file")

    try:
        cap=cv2.VideoCapture(video_file)
    except FileNotFoundError:
        print("Cannot locate video file: "+ video_file)
    except Exception as e:
        print("Something else went wrong with the video file: ", e)
    
    initial_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    initial_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_len = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    out_video = cv2.VideoWriter(os.path.join(output_path, 'output_video.mp4'), cv2.VideoWriter_fourcc(*'avc1'), fps, (initial_w, initial_h), True)
    
    counter=0
    start_inference_time=time.time()

    try:
        while cap.isOpened():
            ret, frame=cap.read()
            if not ret:
                break
            counter+=1
            
            coords, image= pd.predict(frame)
            num_people= queue.check_coords(coords)
            print(f"Total People in frame = {len(coords)}")
            print(f"Number of people in queue = {num_people}")
            out_text=""
            y_pixel=25
            
            for k, v in num_people.items():
                out_text += f"No. of People in Queue {k} is {v} "
                if v >= int(max_people):
                    out_text += f" Queue full; Please move to next Queue "
                cv2.putText(image, out_text, (15, y_pixel), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                out_text=""
                y_pixel+=40
            out_video.write(image)
            
        total_time=time.time()-start_inference_time
        total_inference_time=round(total_time, 1)
        fps=counter/total_inference_time

        with open(os.path.join(output_path, 'stats.txt'), 'w') as f:
            f.write(str(total_inference_time)+'\n')
            f.write(str(fps)+'\n')
            f.write(str(total_model_load_time)+'\n')

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Could not run Inference: ", e)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    parser.add_argument('--device', default='CPU')
    parser.add_argument('--video', default=None)
    parser.add_argument('--queue_param', default=None)
    parser.add_argument('--output_path', default='/results')
    parser.add_argument('--max_people', default=2)
    parser.add_argument('--threshold', default=0.60)
    
    args=parser.parse_args()

    main(args)