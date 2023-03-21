# Mysterious-Learning

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: One day the archeologist came across a strange metal plate covered in uncommon hieroglyphics. It looked like blueprints for some kind of alien technology. "What kind of magic is this?" He studied the plate more closely and was amazed by the advanced technology and incredible engineering they were using at a time like this. This could only lead him in him wanting to learn more...

## NOTES

1. Extract files
   1. > unzip ml_mysterious_learnings.zip
      1. FILE(S): alien.h5
2. Examine files
   1. > file alien.h5
      1. RESPONSE: `alien.h5: Hierarchical Data Format (version 5) data`
   2. > strings alien.h5

        ```text
            {"class_name": "Sequential", "config": {"name": "19oNHJkX3RvX3V", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": [null, 32, 32, 3], "dtype": "float32", "sparse": false, "ragged": false, "name": "conv2d_3_input"}}, {"class_name": "Conv2D", "config": {"name": "conv2d_3", "trainable": true, "dtype": "float32", "batch_input_shape": [null, 32, 32, 3], "filters": 32, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "MaxPooling2D", "config": {"name": "max_pooling2d_2", "trainable": true, "dtype": "float32", "pool_size": [2, 2], "padding": "valid", "strides": [2, 2], "data_format": "channels_last"}}, {"class_name": "Conv2D", "config": {"name": "conv2d_4", "trainable": true, "dtype": "float32", "filters": 64, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "MaxPooling2D", "config": {"name": "max_pooling2d_3", "trainable": true, "dtype": "float32", "pool_size": [2, 2], "padding": "valid", "strides": [2, 2], "data_format": "channels_last"}}, {"class_name": "Conv2D", "config": {"name": "conv2d_5", "trainable": true, "dtype": "float32", "filters": 64, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Lambda", "config": {"name": "uZDNyc3Q0bmR9", "trainable": true, "dtype": "float32", "function": ["4wEAAAAAAAAAAAAAAAEAAAABAAAAQwAAAHMEAAAAfABTACkBTqkAKQHaAXhyAQAAAHIBAAAA+h88\naXB5dGhvbi1pbnB1dC0xMi02ZGI4ZTVhZTA2ZGE+2gg8bGFtYmRhPggAAADzAAAAAA==\n", null, null], "function_type": "lambda", "module": "__main__", "output_shape": null, "output_shape_type": "raw", "output_shape_module": null, "arguments": {}}}, {"class_name": "Flatten", "config": {"name": "flatten_1", "trainable": true, "dtype": "float32", "data_format": "channels_last"}}, {"class_name": "Dense", "config": {"name": "dense_2", "trainable": true, "dtype": "float32", "units": 64, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_3", "trainable": true, "dtype": "float32", "units": 10, "activation": "linear", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Lambda", "config": {"name": "lambda_1", "trainable": true, "dtype": "float32", "function": ["4wEAAAAAAAAAAAAAAAEAAAACAAAAQwAAAHMMAAAAdABkAYMBAQB8AFMAKQJO2g1TRlJDZTI0d2RG\nOXpiKQHaBXByaW50KQHaAXipAHIEAAAA+h88aXB5dGhvbi1pbnB1dC0xMS1kNTY5YzRhOTUyYjQ+\n2gltYWxpY2lvdXMCAAAAcwQAAAAAAQgB\n", null, null], "function_type": "lambda", "module": "__main__", "output_shape": null, "output_shape_type": "raw", "output_shape_module": null, "arguments": {}}}]}}
            {"loss": {"class_name": "SparseCategoricalCrossentropy", "config": {"reduction": "auto", "name": "sparse_categorical_crossentropy", "from_logits": true, "ignore_class": null}}, "metrics": [[{"class_name": "MeanMetricWrapper", "config": {"name": "accuracy", "dtype": "float32", "fn": "sparse_categorical_accuracy"}}]], "weighted_metrics": null, "loss_weights": null, "optimizer_config": {"class_name": "Custom>Adam", "config": {"name": "Adam", "weight_decay": null, "clipnorm": null, "global_clipnorm": null, "clipvalue": null, "use_ema": false, "ema_momentum": 0.99, "ema_overwrite_frequency": null, "jit_compile": false, "is_legacy_optimizer": false, "learning_rate": 0.0010000000474974513, "beta_1": 0.9, "beta_2": 0.999, "epsilon": 1e-07, "amsgrad": false}}}
        ```

        1. This almost looks like JSON

   3. What is .h5 file?
      1. *An H5 file is a data file saved in the Hierarchical Data Format (HDF). It contains multidimensional arrays of scientific data. H5 files are commonly used in aerospace, physics, engineering, finance, academic research, genomics, astronomy, electronics instruments, and medical fields.* - Credit <fileinfo.com>
   4. H5PY
      1. It looks like there is a python library to help read the data file
      2. Lets create a script
3. PYTHON
   1. Lets create a script to view & potentially understand the data
   2. We will want to import the h5py library
   3. First iteration of our script we look at the f.keys()
      1. `model_weights`
      2. `optimizer_weights`
         1. These look to bee our highest level on the heirarchy
   4. Now lets iterate through each of these an get their respective keys
4. H5DUMP
   1. There is another tool called h5dump that will dump out all the data organized
      1. > h5dump alien.h5 > h5dump.txt
