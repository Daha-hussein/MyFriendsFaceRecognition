if __model is not None:
    result.append({
        'class': class_number_to_name(__model.predict(final)[0]),
        'class_probability': np.around(__model.predict_proba(final)*100,2).tolist()[0],
        'class_dictionary': __class_name_to_number
    })
else:
    print("Model is not loaded or initialized.")