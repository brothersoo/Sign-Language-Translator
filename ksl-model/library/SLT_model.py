from keras import regularizers
from keras import layers
from keras.models import Sequential

def GRU_RNN(n_input_, n_hidden_, n_classes_, lambda_loss_amount_, batch_size_, n_steps):
    return Sequential([
        # relu activation
        layers.Dense(n_hidden_, activation='relu', 
            kernel_initializer='random_normal', 
            bias_initializer='random_normal',
            batch_input_shape=(batch_size_, n_steps, n_input_)
        ),
        layers.GRU(n_hidden_, return_sequences=True),
        layers.Dropout(0.2),
        layers.GRU(n_hidden_, return_sequences=True),
        layers.GRU(n_hidden_, return_sequences=True),
        layers.GRU(n_hidden_, return_sequences=True),
        layers.GRU(n_hidden_),

        layers.Dense(n_classes_, kernel_initializer='random_normal', 
            bias_initializer='random_normal',
            kernel_regularizer=regularizers.l2(lambda_loss_amount_),
            bias_regularizer=regularizers.l2(lambda_loss_amount_),
            activation='softmax'
        )
    ])