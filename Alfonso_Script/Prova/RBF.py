import numpy as np
import Kmeans

class RBF:

    def __init__(self, X, y, tX, ty, num_of_classes,k, std_from_clusters):
        self.X = X
        self.y = y

        self.tX = tX
        self.ty = ty

        self.number_of_classes = num_of_classes
        self.k = k
        self.std_from_clusters = std_from_clusters

#ritorna la funzione di attivazione del punto x
    def rbf(self, x, c, s):
        return  np.exp(-s*np.linalg.norm(c-x)**2)

#ritorna una lista di funzoioni di attivazioni
    def rbf_list(self, X, centroids, std_list):
        RBF_list = []
        for x in X:
            RBF_list.append([self.rbf(x, c, s) for (c, s) in zip(centroids, std_list)])
        return np.array(RBF_list)

#funzione di adattamento 
    def fit(self):
#RBF_X è la matrice con X_training
#RBF_list_test è la matrice di test
        self.centroids, self.std_list = Kmeans.kmeans(self.X, self.k, max_iters=1000)

#        if not self.std_from_clusters:
#           dMax = np.max([Kmeans.get_distance(c1, c2) for c1 in self.centroids for c2 in self.centroids])
#           self.std_list = np.repeat(dMax / np.sqrt(2 * self.k), self.k)

        RBF_X = self.rbf_list(self.X, self.centroids, self.std_list)
        #Calcola la regressione lineare per sapere il peso
        self.w = np.linalg.pinv(RBF_X.T @ RBF_X) @ RBF_X.T @ self.y

        RBF_list_tst = self.rbf_list(self.tX, self.centroids, self.std_list)


        self.pred_ty = RBF_list_tst @ self.w

        #self.pred_ty = np.array([np.argmax(x) for x in self.pred_ty])

        diff = self.pred_ty - self.ty

        print('Accuracy: ', len(np.where(diff == 0)[0]) / len(diff))

