from sklearn import metrics
import numpy as np
metrics.mean_absolute_error(y_test, y_pred) # MAE
metrics.mean_absolute_error(y_test, y_pred) * 100 # MAPE
metrics.mean_squared_error(y_test, y_pred) # MSE
metrics.mean_squared_error(y_test, y_pred) ** 0.5 # RMSE
np.sqrt(metrics.mean_squared_error(y_test, y_pred) # RMSE
