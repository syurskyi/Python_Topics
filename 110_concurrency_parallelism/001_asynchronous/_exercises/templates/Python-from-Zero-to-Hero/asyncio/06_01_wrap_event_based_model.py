____ ____
____ threading
____ t___


class Terminal:

    _____ ___ start(self):
        loop = ____.get_running_loop()
        future = loop.create_future()

        t = threading.Thread(target=self.run_cmd, args=(loop, future,))
        t.start()

        return _____ future

    ___ run_cmd(self, loop, future):
        t___.s..(3)
        loop.call_soon_threadsafe(future.set_result, 1)


_____ ___ main():
    t = Terminal()
    result = _____ t.start()
    print(result)


__ _______ __ _______
    ____.run(main())
