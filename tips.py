# A comprehensive dictionary of tips based on hazard type
HEALTH_TIPS = {
    "high_temperature": (
        "**High Temperature Alert:**\n"
        "- **Stay Hydrated:** Drink plenty of water throughout the day, even if you don't feel thirsty.\n"
        "- **Avoid Peak Sun Hours:** Limit outdoor activities between 10 a.m. and 4 p.m.\n"
        "- **Seek Cool Environments:** Stay in air-conditioned places. If you don't have AC, visit public places like libraries or malls.\n"
        "- **Dress Lightly:** Wear lightweight, loose-fitting, and light-colored clothing."
    ),
    "low_temperature": (
        "**Low Temperature Alert:**\n"
        "- **Dress in Layers:** Wear multiple layers of warm clothing to trap heat.\n"
        "- **Protect Extremities:** Use hats, gloves, and warm socks to protect your head, hands, and feet from frostbite.\n"
        "- **Limit Exposure:** Spend as little time as possible outdoors in extreme cold."
    ),
    "high_humidity": (
        "**High Humidity Alert:**\n"
        "- **Control Indoor Climate:** Use a dehumidifier to reduce moisture and prevent mold growth.\n"
        "- **Ensure Ventilation:** Keep air circulating with fans or open windows to make the environment feel cooler."
    ),
    "low_humidity": (
        "**Low Humidity Alert:**\n"
        "- **Moisturize:** Use a humidifier to add moisture to the air, which helps prevent dry skin, itchy eyes, and irritated sinuses.\n"
        "- **Stay Hydrated:** Drink water to keep your body hydrated from the inside out."
    ),
    "high_co2": (
        "**Elevated CO2 Alert:**\n"
        "- **Increase Ventilation:** This is crucial. Open windows and doors to bring in fresh air and dilute indoor CO2 levels.\n"
        "- **Check Your Systems:** Ensure your HVAC system's fresh air intake is open and not blocked.\n"
        "- **Consider an Air Purifier:** Use a purifier with a HEPA filter to help circulate and clean the air."
    ),
    "high_co": (
        "**URGENT: High Carbon Monoxide Detected:**\n"
        "- **Evacuate Immediately:** CO is a colorless, odorless, and highly toxic gas. Leave the building immediately.\n"
        "- **Call for Help:** Once you are in a safe location, call your local emergency services (e.g., 911).\n"
        "- **Do Not Re-enter:** Wait for professionals to declare the area safe."
    ),
    "high_pm25": (
        "**High PM2.5 (Fine Particulate Matter) Alert:**\n"
        "- **Wear a Mask:** When outdoors, wear a high-quality, well-fitting mask (like an N95 or KN95) to filter out fine particles.\n"
        "- **Use Air Purifiers:** Run an air purifier with a HEPA filter indoors to capture fine particles.\n"
        "- **Avoid Strenuous Activity:** Reduce intense physical exertion, especially outdoors, to lower your inhalation rate."
    ),
    "high_pm10": (
        "**High PM10 (Coarse Particulate Matter) Alert:**\n"
        "- **Limit Outdoor Time:** Reduce time spent outdoors, especially near high-traffic areas or industrial zones.\n"
        "- **Keep Windows Closed:** Prevent outdoor dust and particles from entering your home.\n"
        "- **Clean Indoors:** Dust and vacuum regularly to remove particles that have settled."
    ),
    "default": "**All Clear:**\n- All readings are within normal ranges. It's a good day to enjoy the outdoors!",
}


def get_tips(alerts):
    """Returns a list of relevant health tips based on active alerts."""
    if not alerts:
        return [HEALTH_TIPS["default"]]

    tips = set()  # Use a set to avoid duplicate tips
    for alert in alerts:
        # Example alert: "ALERT: Temperature is too high: 38.50 > 35"
        parts = alert.split(" ")
        metric = parts[1].lower()
        condition = "high" if "high" in alert else "low"

        tip_key = f"{condition}_{metric}"
        if tip_key in HEALTH_TIPS:
            tips.add(HEALTH_TIPS[tip_key])

    return sorted(list(tips)) if tips else [HEALTH_TIPS["default"]]
