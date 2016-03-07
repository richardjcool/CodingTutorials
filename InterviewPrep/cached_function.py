"""
Create a function Demo taht takes input a function f and a parameter k
and returns a function that behaves the same as f except it caches the
last k distinct accessed results of f.

EXAMPLE:
    demo_f = Demo(f, 2)
    demo_f(arg1) = computed and cached
    demo_f(arg1) = returned from cache
    demo_f(arg2) = computed and cached
    demo_f(arg3) = computed and cached, f(arg1) is evicted
"""


def Demo(f, size):
    cached_vals = {}
    cached_args = []

    def wrapped(*args):
        # Was this value already cached?
        if args in cached_args:
            return cached_vals[args]

        print("Calculating")
        result = f(*args)

        # Check the size of our cache. If it's the max size
        # remove the first
        if len(cached_args) == size:
            removed_arg = cached_args.pop()
            del cached_vals[removed_arg]

        cached_args.insert(0, args)
        cached_vals[args] = result

        return result

    return wrapped

if __name__ == "__main__":

    def f(x):
        return x**2

    demo_f = Demo(f, 3)
    print(demo_f(1))
    print(demo_f(1))
    print(demo_f(2))
    print(demo_f(3))
    print(demo_f(10))
    print(demo_f(1))
    print(demo_f(10))
