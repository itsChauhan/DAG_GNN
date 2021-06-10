 
class CONFIG:
    """Dataclass with app parameters"""

    def __init__(self):
        pass

    data_filename = "alarm.csv"


    # You must change this to the filename you wish to use as input data

    # Epochs
    epochs = 100

    # Batch size (note: should be divisible by sample size, otherwise throw an error)
    batch_size = 200

    # Learning rate (baseline rate = 1e-3)
    lr = 1e-3

    x_dims = 1
    z_dims = 1
    optimizer = "Adam"
    graph_threshold = 0.3
    tau_A = 0.0
    lambda_A = 0.0
    c_A = 1
    use_A_connect_loss = 0
    use_A_positiver_loss = 0
    no_cuda = False
    seed = 42
    encoder_hidden = 64
    decoder_hidden = 64
    temp = 0.5
    k_max_iter = 101
    encoder = "mlp"
    decoder = "mlp"
    no_factor = False
    encoder_dropout = 0.0
    decoder_dropout = (0.0,)
    h_tol = 1e-8
    lr_decay = 200
    gamma = 1.0
    prior = False
