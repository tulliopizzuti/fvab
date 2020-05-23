import numpy as np

#calcola la distanza tra il punto x2 e il centroide x1
def get_distance(x1, x2):
    sum = 0
    for i in range(len(x1)):
        sum += (x1[i] - x2[i]) ** 2
    return np.sqrt(sum)


def kmeans(X, k, max_iters):
    #crea un array centroids con k valori di X presi a caso tra tutti i valori di X
    centroids = X[np.random.choice(range(len(X)), k)]

    converged = False

    current_iter = 0

    while (not converged) and (current_iter < max_iters):
        #crea un arry con tot array vuoti quanti sono gli elementi in centroids
        cluster_list = [[] for i in range(len(centroids))]

        for x in X: #prende ogni dato del dataset
            distances_list = []
            #si calocla la distanza tra il centoride c e il dato x
            for c in centroids:
                distances_list.append(get_distance(c, x))
            #mette x nel clouster che ha la distanza minima da quel punto
            cluster_list[int(np.argmin(distances_list))].append(x)

        cluster_list = list((filter(None, cluster_list)))

        prev_centroids = centroids.copy()

        centroids = []

        for j in range(len(cluster_list)):
            #fa la media di ogni clouster
            centroids.append(np.mean(cluster_list[j], axis=0))

        pattern = np.abs(np.sum(prev_centroids) - np.sum(centroids))

        print('K-MEANS: ', int(pattern))

        converged = (pattern == 0)

        current_iter += 1
    #se il clouset ottenuto è uguale a quello precedente ritorna l'attuale cloouster e un array con
    #la deviazione standard dei elemnti dei clouster
    return np.array(centroids), [np.std(x) for x in cluster_list]