/* Given a string and “ab”, determine if the string can be generated by “ab”. If it can form, then return true or else return false. Initial assumption is that the given input string will only contain characters ‘a’ and ‘b’.
Examples:
“aaabbb” – true
“caabb” – false
“abababab” – true
“aaabbbb” – false

Also,consider the input array having other characters than ‘a’ and ‘b’ as well.
*/

pattern = "abcabcaabbcc"
result = []
for i in pattern:
  count = pattern.count(i)
  if count not in result:
     result.append(count)
if len(result) > 1:
   print False
else:
   print True