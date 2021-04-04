{
  'targets': [
    {
      "target_name": "kinectAzure",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "src/kinect_azure.cc" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<(module_root_dir)/sdk/sensor-sdk-1.4.1/build/native/include",
        # "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/build/native/include"
        "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/sdk/include"

      ],
      "libraries": [
        "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4a.lib",
        "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4arecord.lib",
        # "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/lib/native/amd64/release/k4abt.lib"
        "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/sdk/windows-desktop/amd64/release/lib/k4abt.lib"
      ],
      "copies": [
        {
          "destination": "<(module_root_dir)/build/Release",
          "files": [
            "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/depthengine_2_0.dll",
            "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4a.dll",
            "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4arecord.dll",

            # "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/lib/native/amd64/release/k4abt.dll",
            # "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/lib/native/amd64/release/onnxruntime.dll",
            # "<(module_root_dir)/sdk/body-tracking-sdk-1.0.1/content/dnn_model_2_0.onnx",
            # "<(module_root_dir)/sdk/body-tracking-dependencies/lib/native/amd64/release/cublas64_100.dll",
            # "<(module_root_dir)/sdk/body-tracking-dependencies/lib/native/amd64/release/cudart64_100.dll",
            # "<(module_root_dir)/sdk/body-tracking-dependencies/lib/native/amd64/release/vcomp140.dll",
            # "<(module_root_dir)/sdk/cudnn/lib/native/amd64/release/cudnn64_7.dll",

            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/k4abt.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/onnxruntime.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/dnn_model_2_0_op11.onnx",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/dnn_model_2_0_lite_op11.onnx",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cublas64_11.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cublasLt64_11.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cudart64_110.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/vcomp140.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cudnn64_8.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cudnn_cnn_infer64_8.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cudnn_ops_infer64_8.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/cufft64_10.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/directml.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/myelin64_1.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/nvinfer.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/nvinfer_plugin.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/nvrtc64_111_0.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/nvrtc-builtins64_111.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/onnxruntime_providers_shared.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-Body-Tracking-SDK-1.1.0/tools/onnxruntime_providers_tensorrt.dll",




          ]
        }
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}
