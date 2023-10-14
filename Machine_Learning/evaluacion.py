scores=model.evaluate(training_data, target_data)
print("\n%s:%.2f%%"%(model.metrics_names[1], scores[1]*100))