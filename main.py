from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    answer = {}
    for user in users:
        date_transformed = datetime(date.today().year, user["birthday"].month, user["birthday"].day).date()
        if date_transformed < date.today():
            date_transformed = datetime(date.today().year + 1, user["birthday"].month, user["birthday"].day).date()
        if date_transformed >= date.today():
            if date_transformed - date.today() <= timedelta(days=6):
                if date_transformed.weekday() >= 5:
                    if "Monday" in answer:
                        answer["Monday"].append(user["name"])
                    else:
                        answer["Monday"] = [user["name"]]
                else:
                    if f"{date_transformed:%A}" in answer:
                        answer[f"{date_transformed:%A}"].append(user["name"])
                    else:
                        answer[f"{date_transformed:%A}"] = [user["name"]]
    return answer


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
