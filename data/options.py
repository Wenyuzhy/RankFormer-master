import argparse

def option():
    # Training settings
    parser = argparse.ArgumentParser(description='Retinex')
    parser.add_argument('--batchSize', type=int, default=12, help='training batch size')
    parser.add_argument('--cropSize', type=int, default=256, help='image crop size (patch size)')
    parser.add_argument('--nEpochs', type=int, default=500, help='number of epochs to train for end')
    parser.add_argument('--start_epoch', type=int, default=0, help='number of epochs to start, >0 is retrained a pre-trained pth')
    parser.add_argument('--snapshots', type=int, default=1, help='Snapshots for save checkpoints pth')
    parser.add_argument('--lr', type=float, default=4e-4, help='Learning Rate')
    parser.add_argument('--gpu_mode', type=bool, default=True)
    parser.add_argument('--threads', type=int, default=16, help='number of threads for dataloader to use')

    # choose a scheduler
    parser.add_argument('--cos_restart_cyclic', type=bool, default=False)
    parser.add_argument('--cos_restart', type=bool, default=True)

    # warmup training
    parser.add_argument('--warmup_epochs', type=int, default=3, help='warmup_epochs')
    parser.add_argument('--start_warmup', type=bool, default=True, help='turn False without warmup') 
    
    #model parameter
    parser.add_argument('--model', type=str, default='sfmnet')
    parser.add_argument('--act', type=str, default='PReLU')
    parser.add_argument('--data_range', type=float, default=1)
    parser.add_argument('--num_channels', type=int, default=3)
    parser.add_argument('--num_features', type=int, default=64)
    parser.add_argument('--n_feats', type=int, default=64, help='number of feature maps')
    parser.add_argument('--res_scale', type=float, default=0.2, help='residual scaling')
    parser.add_argument('--base_num_every_group', type=int, default=2, help='super resolution scale')
    parser.add_argument('--scale', type=int, default=8, help='super resolution scale')
    parser.add_argument('--device', default='cuda')

    # train datasets
    parser.add_argument('--data_train_lol_blur'     , type=str, default='./datasets/LOL_blur/train')
    parser.add_argument('--data_train_lol_v1'       , type=str, default='./datasets/LOL_v1/our485')
    parser.add_argument('--data_train_lolv2_real'   , type=str, default='./datasets/LOLv2/Real_captured/Train')
    parser.add_argument('--data_train_lolv2_syn'    , type=str, default='./datasets/LOLv2/Synthetic/Train')
    parser.add_argument('--data_train_SID'          , type=str, default='./datasets/Sony_total_dark/train')
    parser.add_argument('--data_train_SICE'         , type=str, default='./datasets/SICE/Dataset/train')

    # validation input
    parser.add_argument('--data_val_lol_blur'       , type=str, default='./datasets/LOL_blur/eval/low_blur')
    parser.add_argument('--data_val_lol_v1'         , type=str, default='./datasets/LOL_v1/eval15/low')
    parser.add_argument('--data_val_lolv2_real'     , type=str, default='./datasets/LOLv2/Real_captured/Test/Low')
    parser.add_argument('--data_val_lolv2_syn'      , type=str, default='./datasets/LOLv2/Synthetic/Test/Low')
    parser.add_argument('--data_val_SID'            , type=str, default='./datasets/Sony_total_dark/eval/short')
    parser.add_argument('--data_val_SICE_mix'       , type=str, default='./datasets/SICE/Dataset/eval/test')
    parser.add_argument('--data_val_SICE_grad'      , type=str, default='./datasets/SICE/Dataset/eval/test')

    # validation groundtruth
    parser.add_argument('--data_valgt_lol_blur'     , type=str, default='./datasets/LOL_blur/eval/high_sharp_scaled/')
    parser.add_argument('--data_valgt_lol_v1'       , type=str, default='./datasets/LOL_v1/eval15/high/')
    parser.add_argument('--data_valgt_lolv2_real'   , type=str, default='./datasets/LOLv2/Real_captured/Test/Normal/')
    parser.add_argument('--data_valgt_lolv2_syn'    , type=str, default='./datasets/LOLv2/Synthetic/Test/Normal/')
    parser.add_argument('--data_valgt_SID'          , type=str, default='./datasets/Sony_total_dark/eval/long/')
    parser.add_argument('--data_valgt_SICE_mix'     , type=str, default='./datasets/SICE/Dataset/eval/target/')
    parser.add_argument('--data_valgt_SICE_grad'    , type=str, default='./datasets/SICE/Dataset/eval/target/')

    parser.add_argument('--val_folder', default='./validation/', help='Location to save validation datasets')
    
    # # loss weights
    # parser.add_argument('--HVI_weight', type=float, default=1.0)
    # parser.add_argument('--L1_weight', type=float, default=1.0)
    # parser.add_argument('--D_weight',  type=float, default=0.5)
    # parser.add_argument('--E_weight',  type=float, default=50.0)
    # parser.add_argument('--P_weight',  type=float, default=1e-2)
    
    # loss weights
    # parser.add_argument('--HVI_weight', type=float, default=1e-2)
    parser.add_argument('--L1_weight', type=float, default=10.0)
    parser.add_argument('--D_weight',  type=float, default=1e-2)
    parser.add_argument('--E_weight',  type=float, default=1.0)
    parser.add_argument('--P_weight',  type=float, default=1e-3)


    # choose which dataset you want to train, please only set one "True"
    parser.add_argument('--lol_v1', type=bool, default=True)
    parser.add_argument('--lolv2_real', type=bool, default=False)
    parser.add_argument('--lolv2_syn', type=bool, default=False)
    parser.add_argument('--lol_blur', type=bool, default=False)
    parser.add_argument('--SID', type=bool, default=False)
    parser.add_argument('--SICE_mix', type=bool, default=False)
    parser.add_argument('--SICE_grad', type=bool, default=False)
    return parser
