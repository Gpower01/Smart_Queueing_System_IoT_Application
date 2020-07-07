# Manufacturing Project

This task involves deploying the **Smart Queueing System** to a **manufacturing company** to help increase the rate of production and increase revenue. In this very task, the client **Naomi Semiconductors** explains that there have been several roadblocks in their production pipeline. In a normal setting the entire process is belived to take about 6 to 8 weeks-but currently, it is taking 10 to 12 weeks. This is reducing their revenue by 30%.


**Naomi Semiconductor** has noticed that shipping to customers seems to be taking the most time. This part of the production process involves the manual labor of packaging the chips into boxes. There is one particular shop floor -which has two industrial belts-that has shown slower production than the rest.

Workers alternate shifts to keep the floor running 24 hours a day so that packaging continues nonstop, however they have noticed a slow-down in production during the shift transition periods. Between shifts, they observed a 70% dip in the production rate of the package containers.

To help understand and address these issues, Naomi Semiconductor wants a system to monitor the number of people in the factory line. The factory has a vision camera installed at every belt. Each camera records video at 30-35 FPS (Frames Per Second) and this video stream can be used to monitor the number of people in the factory line. Naomi Semiconductor would like the image processing task to be comopleted five times per second.

Once this productivity problem has been addressed, Naomi Seconductor would like to be able to repurpose the system to address a second issue. Ths second issue Naomi Semiconductor has encountered is that a significant percentage of the semiconductor chips being packaged for shipping have flaws. These are not detected until the chips are used by clients. If these flaws could be detected prior to packaging, this would save money and improve the company's reputation.

To be able to detect chip flaws without slowing down the packaging process, the system would need to be able to run inference on the video stream very quickly. Additionally, because there are multiple chip designs-and new designs are created regularly -the system would also need to be flexible so that it can be reprogrammed and optimized to quickly detect flaws in different chip designs.

While Naomi Semiconductors has plenty of revenue to install a quality system, this is still a significant investment and they would ideally like it to last for at least 5-10 years.


# Retail Project 

The client, PriceRight Singapore has one of its smaller outlets in a tiny neighorhood and the store manager wants to use Edge AI to help maximize his profit.

Most of the customers are regulars at the store with an average of about 200 people in the store during weekdays. On the weekends, this increase to between 500 and 1000. The maximum number of people visit the store during the holidays. Most customers spend 30-50 mins in the store during a single visit. Out of this, they have an average wait time of 230 seconds at the checkout counters. But on the weekends, the wait time can increase substantailly. The average time spent is 40 mins at the store and 350-400 sconds at the checkout line. 

The total number of people in the checkout queue ranges from an average of 2 per queue (during normal daily hours) to 5 per queue (during rush hours).

It is during rush hours that PriceRight has seen wavering sales. When wait times are short and checkout happens smoothly, PriceRight sees a jump in his revenue from 6 to 20%. However, if there is congestion at the checkout counter, the profits only goes up to 4-5%.

PriceRight believes this problem can easily be solved by directing people to less-congested queues in the store and they are interested in using an Edge AI system to do so. 

Most of the store's checkout counters already have a modern computer, each of which has an **Intel i7 core processor**. Currently these processors are only used to carry out some minimal tasks that are not computationally expensive.

PriceRight employs close to 300 employees, including staff that work in transportation on the store floor and at the checkout counter. Although the store's annual sales are $7 million in food alone, the net profit is only 1.1% of this. And due to large expenditure in staff wages, PriceRight does not have much money to invest in additional hardware, and also would like to save as much as possible on electric bill.


# Transportation Project

Ms. Leah is the Innovation head for Delhi Metro Rail Services. Delhi Metro is an urban passenger transportation system connecting Ghaziabad, Faridabad, Gurgaon, Noida, Bahadurgarh, and Ballabhgarh in the National Capital Region of India. Delhi Metro makes 2,700 trips every day and is one of the busiest metros in India.

During peak hours, some areas of the platform get highly congested, while other areas remain relatively open. In some cases, passengers trying to board in the more congested areas are unable to get on, even though there is space on the train.

Currently, this congestion is handled manually by door operators, who help direct passengers to less congested areas during peak time. Ms. Leah would like to automate this using an Edge AI system that would monitor the queues in real-time and quickly direct the crowd in the right manner.

In peak hours they currently have over 15 people on average in a single queue outside every door in the Metro Rail. But during non-peak hours, the number of people reduces to 7 people in a single queue. On office hours there is a train every 2 mins. However, on the weekends the time increases to up to 5 mins since some of their drivers work only 5 days a week.

They monitor the entire situation with 7 CCTV cameras on the platform. These are connected to closed All-In-One PCs that are located in a nearby security booth. The CPUs in these machines are currently being used to process and view CCTV footage for security purposes and no significant additional processing power is available to run inference. Ms. Leah's budget allows for a maximum of $300 per machine, and she would like to save as much as possible both on hardware and future power requirements.


























