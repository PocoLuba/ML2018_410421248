我用keras模型來做這次的作業，我用sequential模型，用到的Activation model有relu,softmax，用到的優化器是adam，據說會比較精準所以就拿來用。
訓練參數:
epochs=10, batch_size=200, verbose=2

Training data :
第一次

![Image of first](https://github.com/PocoLuba/ML2018_410421248/blob/master/HW2/first%20training.png?raw=true)

第二次

![Image of second](https://github.com/PocoLuba/ML2018_410421248/blob/master/HW2/second%20training.png?raw=true)

第三次

![Image of third](https://github.com/PocoLuba/ML2018_410421248/blob/master/HW2/third%20training.png?raw=true)

經過三個周期的訓練後，發現驗證的訓練精準度小小增加，然而訓練的資料卻在第三次精準度降低了一點。

第三次的訓練曲線圖:

1.精準度/次數

![Image of graph-1](https://github.com/PocoLuba/ML2018_410421248/blob/master/HW2/Figure_1.png?raw=true)

可以發現訓練第一次與第二次之間有明顯的進步，直到訓練後期漸漸趨緩下來。

2.損失度/次數

![Image of graph-1-1](https://github.com/PocoLuba/ML2018_410421248/blob/master/HW2/Figure_1-1.png?raw=true)

 在訓練後期, "loss 訓練的誤差" 比 "val_loss 驗證的誤差" 小
 兩圖證明不論是訓練與驗證, 誤差越來越低、精準越來越高。
