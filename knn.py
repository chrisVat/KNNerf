import torch
import numpy as np
import os


class KNN(object):
    def __init__(self, k, pos_path, index_path, labels):
        self.k = k
        self.tx_pos = np.loadtxt(os.path.join(pos_path), delimiter=',', skiprows=1)
        self.indexes  = np.loadtxt(index_path, dtype=np.int32)
        self.positions = self.tx_pos[self.indexes-1]
        self.labels = labels 
        # convert to numpy from torch
        self.labels = np.array(self.labels)
        self.labels = self.labels.reshape(self.indexes.shape[0], -1)
        print("Labels: ", self.labels.shape)

    def predict(self, poses):
        num_examples = poses.shape[0]
        target_shape = self.labels[0].shape
        shape = (num_examples,) + target_shape
        y_pred = np.zeros(shape)

        for i in range(num_examples):
            distances = np.sum(np.abs(self.positions - poses[i]), axis=1)
            min_indexes = np.argsort(distances)[:self.k]
            items = self.labels[min_indexes]
            # print(items)
            average = np.mean(items, axis=0)
            y_pred[i] = average
        # convert to torch
        y_pred = torch.from_numpy(y_pred)
        # print("ypred: ", y_pred)
        # print("ypred shape: ", y_pred.shape)

        return y_pred

