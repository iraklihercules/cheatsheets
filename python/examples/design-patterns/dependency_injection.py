# DependencyInjector: This class provides methods for registering dependencies and injecting dependencies into classes.
# - register: Registers dependencies with a unique name.
# - inject: This decorator is used to inject dependencies into a class. It dynamically injects dependencies based on
# the __dependencies__ attribute of the class.

# NotificationService: This class represents a service that sends notifications. It has a send_notification() method
# that depends on an EmailService instance to send emails.

# EmailService: This class represents a service that sends emails. It has a send_email() method.

# Example usage: The NotificationService class is decorated with the DependencyInjector.inject decorator, which
# injects dependencies specified in the __dependencies__ attribute. In this case, it injects an EmailService instance.

# Register dependencies: Dependencies are registered using the DependencyInjector.register method.

# Client code: In the client code, an instance of NotificationService is created, and the send_notification() method
# is called. The NotificationService class automatically gets its dependencies injected.

# This example demonstrates how the dependency injection pattern can be implemented in Python using a decorator.
# It allows for decoupling of dependencies and promotes flexibility and testability in the codebase.

class DependencyInjector:
    _dependencies = {}

    @classmethod
    def register(cls, dependency_name, dependency):
        cls._dependencies[dependency_name] = dependency

    @classmethod
    def inject(cls, dependent_cls):
        def inject_dependencies(*args, **kwargs):
            for attr_name, dependency_name in getattr(dependent_cls, '__dependencies__', {}).items():
                if dependency_name in cls._dependencies:
                    setattr(args[0], attr_name, cls._dependencies[dependency_name])
            return dependent_cls(*args, **kwargs)
        return inject_dependencies


# Example usage
@DependencyInjector.inject
class NotificationService:
    __dependencies__ = {'email_service': 'EmailService'}

    def send_notification(self, recipient, message):
        self.email_service.send_email(recipient, message)


class EmailService:
    def send_email(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


# Register dependencies
DependencyInjector.register('EmailService', EmailService())


# Client code
if __name__ == "__main__":
    notification_service = NotificationService()
    notification_service.send_notification("example@example.com", "Hello, world!")
