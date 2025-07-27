from config import DEFAULT_THRESHOLDS
from db_handler import get_thresholds

def check_thresholds(latest_data):
    """Checks the latest data against safety thresholds and returns alerts."""
    alerts = []
    user_thresholds = get_thresholds()

    # Merge user thresholds with defaults, giving user settings precedence
    thresholds = DEFAULT_THRESHOLDS.copy()
    for metric, values in user_thresholds.items():
        if metric in thresholds:
            thresholds[metric].update(values)
        else:
            thresholds[metric] = values

    for metric, value in latest_data.items():
        if value is None:
            continue

        if metric in thresholds:
            limits = thresholds[metric]
            if "max" in limits and value > limits["max"]:
                alerts.append(
                    f"ALERT: {metric.capitalize()} is too high: {value:.2f} > {limits['max']}"
                )
            if "min" in limits and value < limits["min"]:
                alerts.append(
                    f"ALERT: {metric.capitalize()} is too low: {value:.2f} < {limits['min']}"
                )

    return alerts