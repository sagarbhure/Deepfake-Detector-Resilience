def evaluate_detector(detector, dataset):
    # Example: Evaluate detector on a given dataset
    results = []
    for image in dataset:
        prediction = detector.predict(image)
        results.append(prediction)
    return results
