# Self check questions
![[Linux - Intro- multichoice questions.htm]]


# Exercises
Change directory to **/proc**.
1. What CPU(s) is the system running on?
	- `cat /proc/cpuinfo`
2. How much RAM does it currently use?
	- `cat /proc/meminfo`
3. How much swap space do you have?
	- `cat /proc/swaps`
4. What drivers are loaded?
	- `cat /proc/driver/rtc`
	- `cat /proc/driver/nvram`
	![[Pasted image 20240316230658.png]]
5. How many hours has the system been running?
	- `cat /proc/uptime`
6. Which filesystems are known by your system?
	- `cat /proc/filesystems`
	![[Pasted image 20240316230919.png]]

---
Change to `/etc`
1. How long does the system keep the log file in which user logins are monitored?
2. How many users are defined on your system? Don't count them, let the computer do it for you using wc!
3. How many groups do you have?
4. Which version of bash is installed on this system?
5. Where is the time zone information kept?