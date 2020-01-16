# # -*- coding: utf-8 -*-
#
# ______ ____
#
# # Encoding and Decoding Custom Python Objects
# # What happens when we try to serialize the Elf class from that Dungeons & Dragons app you’re working on?
#
#
# c_ Elf
#     ___ - ____ level, ability_scores_N..
#         ____.?   ?
#         ____.? _
#             "str": 11, "dex": 12, "con": 10,
#             "int": 16, "wis": 14, "cha": 13
#         } __ ? __ N.. ____ ?
#         ____.hp _ 10 + ____.? "con"
#
# # Not so surprisingly, Python complains that Elf isn’t serializable (which you’d know if you’ve ever tried to tell an
# # Elf otherwise):
# #
# elf = ? l.. _ 4
# ____.d.. ?
# # TypeError: Object of type 'Elf' is not JSON serializable
# # Although the json module can handle most built-in Python types, it doesn’t understand how to encode customized data
# # types by default. It’s like trying to fit a square peg in a round hole—you need a buzzsaw and parental supervision.
# #
# # Simplifying Data Structures
# # Now, the question is how to deal with more complex data structures. Well, you could try to encode and decode the JSON
# # by hand, but there’s a slightly more clever solution that’ll save you some work. Instead of going straight from
# # the custom data type to JSON, you can throw in an intermediary step.
# # All you need to do is represent your data in terms of the built-in types json already understands. Essentially, you
# # translate the more complex object into a simpler representation, which the json module then translates into JSON.
# # It’s like the transitive property in mathematics: if A = B and B = C, then A = C.
# # To get the hang of this, you’ll need a complex object to play with. You could use any custom class you like,
# # but Python has a built-in type called complex for representing complex numbers, and it isn’t serializable by default.
# # So, for the sake of these examples, your complex object is going to be a complex object. Confused yet?
# #
# z = 3 + 8j
# print(ty.. ?
# # <class 'complex'>
# print(____.d.. ?
# # TypeError: Object of type 'complex' is not JSON serializable
# # Where do complex numbers come from? You see, when a real number and an imaginary number love each other very much,
# # they add together to produce a number which is (justifiably) called complex.
# # A good question to ask yourself when working with custom types is What is the minimum amount of information necessary
# # to recreate this object? In the case of complex numbers, you only need to know the real and imaginary parts,
# # both of which you can access as attributes on the complex object:
# #
# print(z.real)
# # 3.0
# print(z.imag)
# # 8.0
# # Passing the same numbers into a complex constructor is enough to satisfy the __eq__ comparison operator:
#
# print(complex(3, 8) == z)
# # True
#
# # Breaking custom data types down into their essential components is critical to both the serialization
# # and deserialization processes.
# # Encoding Custom Types
# # To translate a custom object into JSON, all you need to do is provide an encoding function to the dump() method’s
# # default parameter. The json module will call this function on any objects that aren’t natively serializable.
# # Here’s a simple decoding function you can use for practice:
# #
# ___ encode_complex z
#     __ isi.. ? comp..
#         r_ ?.re.. ?.im..
#     ____
#         type_name _ ?. -c . -n
#         r_ T.. _ Object of type '?|' is not JSON serializable")
#
# # Notice that you’re expected to raise a TypeError if you don’t get the kind of object you were expecting. This way,
# # you avoid accidentally serializing any Elves. Now you can try encoding complex objects for yourself!
#
# print(____.d.. 9 + 5j d.. _ ?
# # '[9.0, 5.0]'
# # json.dumps(elf, default=encode_complex)
# # TypeError: Object of type 'Elf' is not JSON serializable
# # Why did we encode the complex number as a tuple? Great question! That certainly wasn’t the only choice, nor is it
# # necessarily the best choice. In fact, this wouldn’t be a very good representation if you ever wanted to decode
# # the object later, as you’ll see shortly.
# # The other common approach is to subclass the standard JSONEncoder and override its default() method:
#
# c_ ComplexEncoder(____.J_E
#     ___ default ____ z
#         __ isi.. ? comp..
#             r_ ?.re.. ?.im..
#         ____
#             r_ su__.d.. ?
#
# # Instead of raising the TypeError yourself, you can simply let the base class handle it. You can use this either
# # directly in the dump() method via the cls parameter or by creating an instance of the encoder and calling its
# # encode() method:
# #
# print(____.d.. 2 + 5j c.. _ C..
# # '[2.0, 5.0]'
#
# encoder = C..
# print(?.e.. (3 + 6j))
# # '[3.0, 6.0]'
# #
# # Decoding Custom Types
# # While the real and imaginary parts of a complex number are absolutely necessary, they are actually not
# # quite sufficient to recreate the object. This is what happens when you try encoding a complex number with
# # the ComplexEncoder and then decoding the result:
# #
# complex_json _ ____.d..(4 + 17j, c.. _ ?
# print(____.l.. ?
# # [4.0, 17.0]
#
# # All you get back is a list, and you’d have to pass the values into a complex constructor if you wanted that complex
# # object again. Recall our discussion about teleportation. What’s missing is metadata, or information about the type
# # of data you’re encoding.
# # I suppose the question you really ought ask yourself is What is the minimum amount of information that is
# # both necessary and sufficient to recreate this object?
# # The json module expects all custom types to be expressed as objects in the JSON standard. For variety, you can create
# # a JSON file this time called complex_data.json and add the following object representing a complex number:
#
# {
#     "__complex__": True,
#     "real": 42,
#     "imag": 36
# }
# # See the clever bit? That "__complex__" key is the metadata we just talked about. It doesn’t really matter what
# # the associated value is. To get this little hack to work, all you need to do is verify that the key exists:
#
# ___ decode_complex dct
#     __ "__complex__" __ ?
#         r_ complex ? "real"| ? "imag"?
#     r_ ?
#
# # If "__complex__" isn’t in the dictionary, you can just r_ the object and let the default decoder deal with it.
# # Every time the load() method attempts to parse an object, you are given the opportunity to intercede before
# # the default decoder has its way with the data. You can do this by passing your decoding function to the object_hook parameter.
# # Now play the same kind of game as before:
# #
# w__ o.. complex_data.json __ complex_data
#     data _ ?.r..
#     z = ____.l.. ? o_h. _ ?
# # ...
# print(ty.. z
# # <class 'complex'>
# # While object_hook might feel like the counterpart to the dump() method’s default parameter, the analogy really begins
# # and ends there.
# # This doesn’t just work with one object either. Try putting this list of complex numbers into complex_data.json and
# # running the script again:
#
# [
#   {
#     "__complex__":true,
#     "real":42,
#     "imag":36
#   },
#   {
#     "__complex__":true,
#     "real":64,
#     "imag":11
#   }
# ]
# # If all goes well, you’ll get a list of complex objects:
#
# w___ o.. complex_data.json __ complex_data
#     data _ ?.r..
#     numbers _ ____.l.. ? o_h. _ ?
# # ...
# print(nu..
# # [(42+36j), (64+11j)]
#
# # You could also try subclassing JSONDecoder and overriding object_hook, but it’s better to stick with the lightweight
# # solution whenever possible.
# #
# # All done!
# # Congratulations, you can now wield the mighty power of JSON for any and all of your nefarious Python needs.
# # While the examples you’ve worked with here are certainly contrived and overly simplistic, they illustrate a workflow
# # you can apply to more general tasks:
# #
# # Import the json package.
# # Read the data with load() or loads().
# # Process the data.
# # Write the altered data with dump() or dumps().
# # What you do with your data once it’s been loaded into memory will depend on your use case. Generally, your goal will
# # be gathering data from a source, extracting useful information, and passing that information along or keeping
# # a record of it.
# # Today you took a journey: you captured and tamed some wild JSON, and you made it back in time for supper!
# # As an added bonus, learning the json package will make learning pickle and marshal a snap.
# #
# # Good luck with all of your future Pythonic endeavors!
