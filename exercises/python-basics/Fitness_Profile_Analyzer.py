def get_bmi(weight, height_cm):
    return weight / ((height_cm / 100) ** 2)


def get_age_group(age):
    if age < 10:
        return "under_10"
    elif age < 20:
        return "child_and_adolescent"
    return "adult"


def get_gender_group(gender):
    gender = gender.strip().lower()
    if gender == "female":
        return "female"
    elif gender == "male":
        return "male"
    return "other"


def classify_adult_bmi(bmi):
    if bmi < 18.5:
        return (
            "underweight",
            "Focus on balanced nutrition and regular physical activity to reach a healthier weight.",
        )
    elif bmi < 25:
        return (
            "normal weight",
            "Maintain your routine with balanced nutrition, hydration, sleep, and exercise.",
        )
    elif bmi < 30:
        return (
            "overweight",
            "Increase physical activity and improve food choices to move toward a healthier range.",
        )
    return (
        "obese",
        "Seek guidance from a healthcare professional for a safer and more personalized plan.",
    )


def classify_youth_bmi(age, gender_group, bmi):
    if age < 10:
        return (
            "not classified",
            "For children under 10, BMI should be interpreted by a healthcare professional.",
        )

    if gender_group == "female":
        if 10 <= age < 12:
            if bmi < 14:
                return "underweight", "Focus on balanced nutrition and healthy daily habits."
            elif bmi < 19:
                return "normal weight", "Maintain balanced nutrition and regular physical activity."
            elif bmi < 23.1:
                return "overweight", "Encourage more movement and monitor eating habits."
            return "obese", "Seek professional guidance for safer follow-up and support."

        elif 12 <= age < 15:
            if bmi < 14.8:
                return "underweight", "Focus on balanced nutrition and healthy daily habits."
            elif bmi < 21.8:
                return "normal weight", "Maintain balanced nutrition and regular physical activity."
            elif bmi < 25.8:
                return "overweight", "Encourage more movement and monitor eating habits."
            return "obese", "Seek professional guidance for safer follow-up and support."

        else:
            if bmi < 16.3:
                return "underweight", "Focus on balanced nutrition and healthy daily habits."
            elif bmi < 23.9:
                return "normal weight", "Maintain balanced nutrition and regular physical activity."
            elif bmi < 28.1:
                return "overweight", "Encourage more movement and monitor eating habits."
            return "obese", "Seek professional guidance for safer follow-up and support."

    else:
        if 10 <= age < 12:
            if bmi < 14.2:
                return "underweight", "Focus on balanced nutrition and healthy daily habits."
            elif bmi < 19.3:
                return "normal weight", "Maintain balanced nutrition and regular physical activity."
            elif bmi < 22.1:
                return "overweight", "Encourage more movement and monitor eating habits."
            return "obese", "Seek professional guidance for safer follow-up and support."

        elif 12 <= age < 15:
            if bmi < 15:
                return "underweight", "Focus on balanced nutrition and healthy daily habits."
            elif bmi < 21:
                return "normal weight", "Maintain balanced nutrition and regular physical activity."
            elif bmi < 25.6:
                return "overweight", "Encourage more movement and monitor eating habits."
            return "obese", "Seek professional guidance for safer follow-up and support."

        else:
            if bmi < 16.5:
                return "underweight", "Focus on balanced nutrition and healthy daily habits."
            elif bmi < 23.5:
                return "normal weight", "Maintain balanced nutrition and regular physical activity."
            elif bmi < 26.8:
                return "overweight", "Encourage more movement and monitor eating habits."
            return "obese", "Seek professional guidance for safer follow-up and support."


def get_objective_message(objective):
    objective = objective.strip().lower()

    if objective == "lose weight":
        return "Prioritize calorie control, walking or cardio, and consistency over perfection."
    elif objective == "gain muscle":
        return "Prioritize strength training, good recovery, and sufficient protein intake."
    elif objective == "maintain fitness":
        return "Keep a balanced routine with training, recovery, and steady nutrition habits."
    return "Define a clearer goal to receive more specific guidance."


def get_extra_recommendations(category_bmi, objective):
    tips = []

    if category_bmi in ["overweight", "obese"]:
        tips.append("Try to build consistency with 30 to 45 minutes of activity most days of the week.")
        tips.append("Reduce highly processed foods and sugary drinks when possible.")
    elif category_bmi == "underweight":
        tips.append("Consider increasing calorie intake with nutritious foods and regular meals.")
        tips.append("Strength training can help support healthy weight gain.")
    elif category_bmi == "normal weight":
        tips.append("Focus on maintaining healthy routines instead of making drastic changes.")
        tips.append("Keep sleep, hydration, and movement consistent.")

    if objective == "lose weight":
        tips.append("Track portions and keep your routine simple enough to repeat every week.")
    elif objective == "gain muscle":
        tips.append("Progressive overload in training is one of the main keys for muscle gain.")
    elif objective == "maintain fitness":
        tips.append("A stable routine is usually more effective than extreme short-term effort.")

    return tips


def main():
    print("------------ Personal Fitness Profile Analyzer ------------")

    name = input("What is your name? ").strip()
    age = int(input("What is your age? "))
    weight = float(input("What is your weight in kg? "))
    height = float(input("What is your height in cm? "))
    gender = input("What is your gender? (e.g., male, female, other) ").strip()
    objective = input(
        "What is your fitness objective? (e.g., lose weight, gain muscle, maintain fitness) "
    ).strip()

    bmi = get_bmi(weight, height)
    age_group = get_age_group(age)
    gender_group = get_gender_group(gender)

    if age_group == "adult":
        category_bmi, recommendation = classify_adult_bmi(bmi)
    else:
        category_bmi, recommendation = classify_youth_bmi(age, gender_group, bmi)

    objective_message = get_objective_message(objective)
    extra_recommendations = get_extra_recommendations(category_bmi, objective.strip().lower())

    print("\n------------ Personal Fitness Profile ------------")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Height: {height} cm")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi:.2f}")
    print(f"Age Group: {age_group}")
    print(f"Category: {category_bmi}")
    print(f"Fitness Objective: {objective}")
    print(f"Main Recommendation: {recommendation}")
    
    print(f"Objective Guidance: {objective_message}")

    print("Additional Recommendations:")
    for item in extra_recommendations:
        print(f"- {item}")


while True:
    main()
    option = input("\nWould you like to analyze another profile? (yes/no) ").strip().lower()
    if option != "yes":
        break

print("Thank you for using the Personal Fitness Profile Analyzer! Stay healthy and active!")