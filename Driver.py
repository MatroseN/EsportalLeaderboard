import threading
import Main

main = Main.Main()


def run():
    threading.Timer(600, run).start()
    main.main()


run()