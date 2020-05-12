import threading
import Main

main = Main.Main()


def run():
    threading.Timer(1800.0, run).start()
    main.main()


run()
