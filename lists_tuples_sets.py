courses=['History','physics','computer_Sci']
#see the type
#print(type(courses))
#calculate the length
#print(len(courses))
#check the functions and method on list
#print(dir(courses))
#using append method
#courses.append('English')
#print(courses)
#courses.insert(1,'Social')
#print(courses)
#accessing the elements
#print(courses[0:3:1])
#print(courses[-1])
#courses=['History','physics','computer_Sci']
#courses_art=['Art','commerce']
#print(courses_art)
#courses_art.append(courses)
#print(courses_art)
#courses.remove('History')
#popped=courses.pop()
#print(popped)
#num=[1,2,3,4,5]
#print(sum(num))
courses=['History','physics','computer_Sci']
#courses.sort(reverse=True)
#print(courses)
print(courses.index('physics'))
print('History' in courses)
for items in courses:
	print(items)
for number,items in enumerate(courses,start=1):
	print(number,items)
course_str=("-".join(courses))
print(course_str)
print(course_str.split("-"))

hello_tuple=('History','social','physics')
print(hello_tuple)






















