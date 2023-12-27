# KNNERF, modified version of NERF

Run code with nerf2_runner. Currently it is only set up with the RFID dataset. 
It is also only set up to work with a batchsize of 1, but it might work with more.  
Data has to be downloaded  [Here](https://connectpolyu-my.sharepoint.com/:f:/g/personal/20032132r_connect_polyu_hk/EuAACSdRP4VGgw_9n2IqL84BkY_tWD5TeE9kDT0lvjw6jw?e=ygYEvX).
Put it in data/RFID/.   
So data/RFID/ should contain spectrum/, gateway_info.yml, etc.  


# NeRF<sup>2</sup>: Neural Radio-Frequency Radiance Fields

Thank you for your interest in our work. We're excited to announce that we will gradually release the code and dataset for this project.



## Datasets

### RFID spectrum prediction

Datasets and pretrained models are available at [Here](https://connectpolyu-my.sharepoint.com/:f:/g/personal/20032132r_connect_polyu_hk/EuAACSdRP4VGgw_9n2IqL84BkY_tWD5TeE9kDT0lvjw6jw?e=ygYEvX).



### BLE RSSI prediction

Datasets and pretrained models are available at [Here](https://connectpolyu-my.sharepoint.com/:f:/g/personal/20032132r_connect_polyu_hk/EuAACSdRP4VGgw_9n2IqL84BkY_tWD5TeE9kDT0lvjw6jw?e=ygYEvX).



## Running

### Spectrum prediction

**training the model**

```bash
python nerf2_runner.py --mode train --config configs/rfid-spectrum.yml --dataset_type rfid --gpu 0
```

**Inference the model**

```bash
python nerf2_runner.py --mode test --config configs/rfid-spectrum.yml --dataset_type rfid --gpu 0
```



### RSSI prediction

**training the model**

```bash
python nerf2_runner.py --mode train --config configs/ble-rssi.yml --dataset_type ble --gpu 0
```

**Inference the model**

```bash
python nerf2_runner.py --mode test --config configs/ble-rssi.yml --dataset_type ble --gpu 0
```

**MRI**

```python
python baseline/mri.py
```



## To-Do List

- [ ] NeRF2 for FDD MIMO channel prediction
- [ ] CGAN RSSI prediction baseline
- [ ] Release more datasets
- [ ] Instruction of preparing own datasets
- [ ] Implementation on Taichi to speed up the code


Please stay tuned for updates and feel free to reach out if you have any questions or need further information.


## License

NeRF<sup>2</sup> is MIT-licensed. The license applies to the pre-trained models and datasets as well.

## Citation

If you find the repository is helpful to your project, please cite as follows:

```bibtex
@inproceedings{zhao2023nerf2,
    author = {Zhao, Xiaopeng and An, Zhenlin and Pan, Qingrui and Yang, Lei},
    title = {NeRF2: Neural Radio-Frequency Radiance Fields},
    booktitle = {Proc. of ACM MobiCom '23},
    pages = {1--15},
    year = {2023}
}
```

## Acknowledgment

Some code snippets are borrowed from [nerf-pytorch](https://github.com/yenchenlin/nerf-pytorch) and [NeuS](https://github.com/Totoro97/NeuS).

