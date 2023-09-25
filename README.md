# Traffic Light Simulator Challenge

## Task
Please write a program that draws and operates a traditional traffic light. 
The program should take input from a user about how long each light color should stay lit before transitioning. 
A graphical user interface or CLI ASCII art are equally acceptable. 
Light transitions should be visible to the user. As your software will be used to operate critical infrastructure a user must not be able to crash the software. 
You must provide the user a mechanism for safely exiting your program. You must print ‘Exiting Traffic Light Simulator’ to the screen when the user instructs the program to exit and a different message if the simulator must shut itself down.
You must complete this challenge in Python. You must provide a README file to explain how to build/install and operate your software. 
Your submission must be your own work.
### Evaluation criteria
• You followed instructions <br>
• Software functions as requested and meets all stated requirements <br>
• Software is designed for easy extensibility. Should you proceed to a later round interview, you will be
asked how your software could be modified to accommodate new use cases and traffic light designs.
You will not be provided with descriptions of these variants at this time. <br>
• Software is designed and implemented for automated testability. It is a benefit if this is demonstrated. <br>
• Software is designed and implemented to support packaging and delivery. <br>
• Software conforms to widely accepted coding style guidelines. <br>
• Software is understandable and supportable by a developer other than yourself.

## Solution
1) I have implemented a template class `BaseTrafficLight` with `run()` method in case someone need to implement specific behavior strategies.
An example of a class implementation is a `TrafficLight` which switches signals in the following order: 
`red -> orange -> green`. 
2) I have implemented a template class `BaseUI` for graphical user interface implementation.
3) There is a `GracefulShutdown` class for exiting the app. It receives `SIGINT` and `SIGTERM` signals and gracefully shutdown the app.
4) You can find an example of starting the application in `Makefile`.

If I had more time I would encapsulate the application using `Docker` containerization.<br>
I also was thinking of using `Flask` framework for running an application as a service. <br>
I would implement following routes:
`start`, `shutdown`.
Also, I would use `pytest` for unit testing the modules.


