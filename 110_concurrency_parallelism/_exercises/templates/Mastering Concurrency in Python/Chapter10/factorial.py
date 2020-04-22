______ a..
______ ti..
____ datetime ______ datetime

? ___ custom_factorial(name, n):
    f _ 1

    ___ i __ ra..(2, n + 1):
        print(f'Task {name}: Compute factorial({i}).')
        await ?.s..(1)
        f *_ i

    print(f'Task {name}: factorial({n}) is {f}.')

? ___ main():
    tasks _ [custom_factorial('A', 3), custom_factorial('B', 4)]
    await ?.gather(*tasks)

start _ t__.t__()
?.run(main())
end _ t__.t__()
print(f'Total time: {end - start : .4f}.')
