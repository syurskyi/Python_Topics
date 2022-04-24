#accept both names of the couple
name1,name2=a,b i.. 'Enter the name of a couple of whom you wanna see FUTURE').s..

#remove the similar element from both the string
___ i __ a:
    __ i __ b:
        a a.r..(i,'')
        b b.r..(i,'')

#take the length of the both the strings after removal of the similar characters
length l..(a) + l..(b)

#define a dictionary to simply print the result of the FLAMES
flame_dic {'F':'Friends','L':'Lover','A':'Affectionate','M':'Marriage','E':'Enemies','S':'Sex'}
#define a list to process the flames 
flame =  'F','L','A','M','E','S'

#count to iterate through the flames list
i 0
#count of the length of combined strings
len_count 1
#while there remains only one element in the flames list
w.... l..(flame)!_ 1:
    #if length of the combined string has reached then pop the current element of the flames list
    __ len_count __ length:
        flame.p.. i)
        len_count 1
        #check if after poping the element has the flames reached the end of the list if yes then reset the i counter
        __ i __ l..(flame
            i 0
    ____
        len_count += 1
        i += 1
        #check if the i counter has reached end of the list if yes then reset the counter
        __ i >_ l..(flame
            i 0
print('The relationship future of',name1,'&',name2,' is',flame_dic[flame[0]])
    
    