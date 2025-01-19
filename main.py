def gift_recommender(preference, budget):
    # Make gift options for every preference
    gifts = {
        'electronics': [(100, 'gaming earbuds'), (200, 'headphone'), (float('inf'), 'smart watch')],
        'clothing': [(25, 'tops'), (50, 'jackets'), (100, 'shoes'), (float('inf'), 'suits')],
        'jewelry': [(500, 'ring'), (1000, 'necklace'), (float('inf'), 'bracelet')]
    }
    
    # Make sure preference is in gifts
    if preference in gifts:
        for limit, gift in gifts[preference]:
            if budget <= limit:
                return gift
    # if preference is not in dictionary, just return decorative gifts
    return 'decorative gifts!'

def calculate_student_score (PA, mid_term_exam, final_exam):
    # if student received a 0 on the mid term, replace it with the final exam score
    if mid_term_exam == 0.0:
        mid_term_exam = final_exam
    score = (PA * 0.40) + (mid_term_exam * 0.30) + (final_exam * 0.3)
    if final_exam == 0.0:
        score = 0.0
    return score

def calculate_letter_grade (score):
    if score > 90:
        letter = 'A'
    elif score <= 90.0 and score > 80.0:
        letter = 'B'
    elif score > 70.0 and score <= 80.0:
        letter = 'C'
    elif score >= 60.0 and score <= 70.0:
        letter = 'D'
    else:
        letter = 'F'
    return letter

def is_discount_applicable(age, is_military, major, gpa):
    """
    Determines if a discount is applicable based on age, military status, major, and GPA.

    Parameters are:
        age (int): The age of the customer.
        is_military (bool): if customer is in military.
        major (str): Their major.
        gpa (float): Their GPA.

    Return:
        bool: True if the discount is applicable, False otherwise.
    """
    
    eligible = (
        age >= 60 or                # Seniors
        is_military or              # Military personnel
        (major == 'CS' and gpa >= 3.7)  # CS majors with GPA >= 3.7
    )
    return eligible

def book_price (age, is_military, major, gpa, book_category):
    discount = 0.0
    if is_discount_applicable(age, is_military, major, gpa):
        if book_category == 'comic':#if the book they're getting is a comic book
            price = 15#The price will be 15 dollars
            discount = discount + 0.2#The discount is 20% or 0.2 in decimal form
        elif book_category == 'mystery':#if its a mystery book
            price = 10#The price will be 10 dollars and they dont get a discount
        elif book_category == 'fiction':#If its a fiction book
            price = 30#The price will be 30 dollars
            discount = discount + 0.2#The discount will be 20% or 0.2 as decimal
        elif book_category == 'novel':#if its a novel book
            price = 20#The price will be 20 dollars
            discount = discount + 0.4#and the discount will be 40% or 0.4 
        elif book_category == 'horror':#if its a horror book
            price = 20#The price will be 20 dollars, they get no discount
        elif book_category == 'science':#if its a science book
            price = 30#the price is just 30 and they get no discount
        else:#if the book is any other category
            price = 0#the price will be 0 and they dont get discount
    else:#if they dont qualify for discount, then the price will stay the same
        if book_category == 'science':
            price = 30
        elif book_category == 'fiction':
            price = 30
        elif book_category == 'novel':
            price = 20
        elif book_category == 'horror':
            price = 20
        elif book_category == 'mystery':
            price = 10
        elif book_category == 'comic':
            price = 15
        else:
            price = 0
    discount2 = price * discount#figure out how much money needs to be taken off
    price = price - discount2#Now take that money off of the price
    return price
