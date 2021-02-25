import abc 
import apagar, dormir, encender, hablar
class Bot():
    def __init__(self):
        pass
    
    def exec_command(command: Command):
        return Command.execute


class Command(abc):
    @abstractmethod
    def execute():
        pass

if __name__ == "__main__"
    bot = Bot()
    bot.exec_command(DormirCommand)
