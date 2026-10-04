"Predict one delivery, from the command line."

import pandas as pd

from delivery import load_model


def main():
    # TODO: load work/model.joblib, predict one 7 km / 25 min /
    #       traffic 3 / no rain order, and print "PREDICTION: <minutes>"
    model = load_model("model.joblib")
    X = pd.DataFrame([[7, 25, 3, 0]],
                     columns=["distance_km", "prep_time_min", "traffic_level", "rain"])
    minutes = model.predict(X)[0]
    print(f"PREDICTION: {minutes:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
