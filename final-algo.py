individuals = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'courses': ['COSC 225', 'MATH 150'], 'spot': 3, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Doe', 'courses': ['CHEM 228', 'PHYS 101'], 'spot': 2, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 3, 'first_name': 'Jim', 'last_name': 'Smith', 'courses': ['HIST 007', 'CULP 346'], 'spot': 1, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 4, 'first_name': 'Jane', 'last_name': 'Smith', 'courses': ['CLSS 141', 'CLSL 002'], 'spot': 5, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 5, 'first_name': 'John', 'last_name': 'Johnson', 'courses': ['COSC 225', 'PHYS 101'], 'spot': 4, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 6, 'first_name': 'Jane', 'last_name': 'Johnson', 'courses': ['MATH 150', 'CHEM 228'], 'spot': 2, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 7, 'first_name': 'Jim', 'last_name': 'Brown', 'courses': ['HIST 007', 'CLSS 141'], 'spot': 1, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 8, 'first_name': 'Jane', 'last_name': 'Brown', 'courses': ['CULP 346', 'CLSL 002'], 'spot': 4, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 9, 'first_name': 'John', 'last_name': 'Davis', 'courses': ['COSC 225', 'MATH 150'], 'spot': 3, 'score': 0, 'phone': 78945658745, 'common_courses': []},
    {'id': 10, 'first_name': 'Jane', 'last_name': 'Davis', 'courses': ['CHEM 228', 'PHYS 101'], 'spot': 2, 'score': 0, 'phone': 78945658745, 'common_courses': []},
]
def add_individual(individuals):
    # Inputs
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    courses = input("Enter courses taken (comma-separated, accepted values: 'COSC 225', 'MATH 150', 'CHEM 228', 'PHYS 101', 'HIST 007', 'CULP 346', 'CLSS 141', 'CLSL 002'): ").split(',')
    spot = int(input("Enter favorite study spot (number 1-5): "))
    phone = int(input("Enter phone: "))
    
    # Append to individuals array
    individuals.append({
        'id': len(individuals)+1,
        'first_name': first_name,
        'last_name': last_name,
        'courses': courses,
        'spot': spot,
        'score': 0,
        'phone': phone,
        'common_courses': []
    })
    
    # Calculate scores
    for i in individuals[:-1]:
        for course in courses:
            if course in i['courses']:
                i['score'] += 2
                i['common_courses'].append(course)
        if i['spot'] == spot:
            i['score'] += 1
        elif i['spot'] in [spot-1, spot+1]:
            i['score'] += 0.5
    
    # Sort scores
    individuals.sort(key=lambda x: x['score'], reverse=True)
    
    # Print top 3 individuals
    print("Top 3 individuals:")
    for i in range(3):
        print(f"Name: {individuals[i]['first_name']} {individuals[i]['last_name']}")
        print(f"Score (0-5): {individuals[i]['score']}")
        print(f"Common courses: {', '.join(individuals[i]['common_courses'])}")
        print(f"Phone: {individuals[i]['phone']}")
        print()
        
add_individual(individuals)
