# The Command Pattern is a behavioral design pattern that encapsulates a request as an object,
# thereby allowing parameterization of clients with queues, requests, and operations. It allows for the
# separation of the requester of an action from the object that performs the action, providing greater
# flexibility and decoupling in the system.

# - Command: Defines the interface for executing an operation. It declares a method execute() that
# encapsulates the action to be performed.
# - LightOnCommand: Concrete implementation of the Command interface. It encapsulates the action of
# turning on a light and maintains a reference to the light object (Receiver) that will perform the action.
# - Light: Represents the Receiver, which knows how to perform the requested action (e.g., turn on the light).
# - RemoteControl: Acts as the Invoker, which is responsible for invoking the command. It holds a reference
# to the command object and can press a button to execute the command.
# - Client code: Creates instances of the Light and LightOnCommand classes, configures the RemoteControl
# with the LightOnCommand, and then presses a button on the remote control to execute the command.

# In this example, the Command Pattern allows the requester (RemoteControl) to be decoupled from the object
# that performs the action (Light). The command (LightOnCommand) encapsulates the request to turn on the light,
# allowing for parameterization of the requester with different commands. This promotes flexibility and
# extensibility in the system, as new commands can be added without modifying existing code.

# Command interface
class Command:
    def execute(self):
        pass


# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()


# Receiver
class Light:
    def turn_on(self):
        print("Light is on")


# Invoker
class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        if self._command:
            self._command.execute()


# Client code
if __name__ == "__main__":
    light = Light()
    light_on_command = LightOnCommand(light)

    remote_control = RemoteControl()
    remote_control.set_command(light_on_command)

    remote_control.press_button()  # Output: Light is on
