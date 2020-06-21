
# Counting Elements
A common approach is to consume the list one by one use a data structue such a hash table
to store the occurrences of the items. Although a hash table on average has a great performance in the worst case
it can perform poorly

Suppose we are asked to count the occurrences of integers present in a list. If the range of these
integers is small enough to fit a memory we might be better off using direct addressing in an array

 Using an array instead of a hash table
is possible depending on the type of elements present in the list. Suppose we are asked to count the
occurrences of integers present in a list. If the range of these integers is small enough to fit a memory
we might be better off using direct addressing in an array. In this exampl
the range is between 0 and 9 so we can insert an array of size 10 and then meap each item in the list to
the index of the array, incrementing the value
as we process the list of numbers. Using an array instead of a hash table guarantees that every insurgen
search will have a constant runtime performance. Building the entire frequency table results in a linear
runtime performance, in the worst case. This trick of using an array as our frequency table can also be
used.
if our range contains negative numbers. When this is the case we just need to shift the elements so the
range starts from the zero index. This is simply achieved by adding the negative range to each item.
Here we show an example with a range from - 4 to 5 where we shift everything by 4 so
4 would map to our array at the zero index minus 3 would map to 1 and so on. When our input range
is too large
we cannot use an array as this would result in a huge waste of memory.
Just to give you an example if the input can be any integer typically between 0 and 2 to the power
of 32 using an array would result in our solution consuming something like 16 gigabytes of memory.
In such cases it's better to use other key value data structures such as hash tables or balanced by
an increase.

# Max Counter

that we have five counters.

Initially these counters are initialized to 0.
The instructions that we receive can be of two different types.
It can be an increase of a particular counter or a max counter.
So let's assume we receive n equals 5.
Five counters and walk through a simple list of instructions for this particular problem. The first instruction
that we receive is an increase where X equals 3.
This means that we need to find our third counter and increment it by 1.
So in this case we go to our third counter and we increment that by one resulting in a value of 1.
Next again continuing with our example we receive an increase counter 4.
So we go to our fourth counter and increment this again by 1 leaving a value of also 1.
Again we receive the same increase, increase counter 4.
So this time the counter is increased to 2.
The next instruction is a max counter instruction. What we do in this instruction is that we reset all
the counter values to be the value of our maximum counter.
In this case our maximum counter is 2 represented by counter 4.
So we go through every counter and reset this to the value of to our next instruction is increase of
counter 1.
So we go to counter 1 and we increase this to 3.
Our next instruction is again an increase counter 4.
So we go to the fourth counter and increase this to the value of 3. Again we receive the same increase
of counter 4.
So now our fourth counter has a value of 4.
Once we consume all our instructions
all that's left is to return the result. The result of this problem is the list of counters that
we have just executed. As we have explained before, the problem has two inputs:
one is the number of counters that we want
(in this example it was 5) and the other one is a set of instructions.
This set of instructions is represented in a second parameter where we receive an array. Each element
in the array is a number representing our counter index.
So for example our second element in the array -number 4 - is telling us that we need to increment the fourth
counter. In the same way
our fifth position in the array is saying increase counter number 1, increase the first counter. The
middle entry in our array, number 6, is telling us that we should perform a max counter instruction.
This is when the number in the array is bigger than the number of counters.
In this case we have 6, 6 is bigger than our number of counters (5) so we can understand that
this is a max counter.
Let's now have a look at our function or method signature.
Our function name should be called solution and should take in two parameters; a
the second parameter is simply our set or array of instructions.
These instructions must be performed in the order they are in the array.
So the first entry in the array is the first to be executed
and so on. The first parameter n is simply the size of our counters. In the previous example we have
seen a problem where n was 5, we had 5 counters.
Once we perform our algorithm all we need to do is simply return the array with the counter results.
In our previous example
we would have returned an array containing 3, 2, 2, and 4 and 2.
And that would have given us a correct solution.
Now Codility only mentions that we should implement an efficient solution.
However, the solution for this problem can be computed in order n plus m runtime. Spacetime
we can compute this in order n, n being the size of the array for holding the counters.

# Max Counters Hint 1

Let's walk through an example where we are given to do with five counters.
So we construct an array holding all these counters starting at index at position 0 up to 4 containing 5
counters. We receive a list of instructions that we need to perform on these counters.
Just remember that in our problem each counter is accessed by its ID and the IDs in the problem start
from one.
However, our index in our array starts from 0.
So every time we reference a counter from the instruction we need to subtract 1 from it to find the
index. In our naive solution what we would do is process each instruction one at a time starting from
the first one.
And in this example the first one is to increment counter number 3.
We start with the first instruction, we find counter number three which in our array is at index number
2 and increase it.
Then we move to our next instruction and increment our fourth counter and we do it again on the fourth.
Then we get the max counter instruction.
So what we do here is first find which is the max which in this case is 2 and then get another counter
starting from the left in our array and setting every single counter that we have to a value of 2.
Then we continue processing the rest of the instructions incrementing the first counter,
then the fourth and again the fourth.
The problem with this solution is the max counter operation. In the max counter operation
we go through every single item in our array and set it to the maximum value.
That particular operation requires n steps and in the worst case this turns our our algorithm into a
quadratic one.
The worst case of our naive algorithm is when every single instruction that we have is a max counter
operation.
When this happens we have to do that linear scan for every instruction that we have.
So if we have m instructions we will end up having m times n operations. We need to find something
faster.
And as usual I'm going to make use of an analogy to help you
solve this particular problem. In our analogy our counters are placed on a virtual racetrack.
How far they get along in the race depends on the value of that particular counter.
So as usual we start processing our instructions and every time we get an increase for a counter we
advance the counter one position.
When we get a max counter operation we do something different.
Instead of setting all the counters to be at exactly the same position what we do is we move the starting
line.
We move the starting line to the front of our fastest runner, in effect restarting the race again.
It's not really fair
on the other counters but it helps us solve our problem.
