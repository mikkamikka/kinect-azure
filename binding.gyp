{
  'targets': [
    {
      "target_name": "kinectAzure",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "src/kinect_azure.cc" ],
      "variables": {
        "body_tracking_sdk_dir": "C:/Program Files/Azure Kinect Body Tracking SDK"
      },
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<(module_root_dir)/sdk/Azure-Kinect-SDK-v1.4.1/sdk/include",
        "<(body_tracking_sdk_dir)/sdk/include"

      ],
      "libraries": [
        "<(module_root_dir)/sdk/Azure-Kinect-SDK-v1.4.1/sdk/windows-desktop/amd64/release/lib/k4a.lib",
        "<(module_root_dir)/sdk/Azure-Kinect-SDK-v1.4.1/sdk/windows-desktop/amd64/release/lib/k4arecord.lib",
         "<(body_tracking_sdk_dir)/sdk/windows-desktop/amd64/release/lib/k4abt.lib"
      ],
      "copies": [
        {
          "destination": "<(module_root_dir)/build/Release",
          "files": [

            "<(module_root_dir)/sdk/Azure-Kinect-SDK-v1.4.1/tools/depthengine_2_0.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-SDK-v1.4.1/tools/k4a.dll",
            "<(module_root_dir)/sdk/Azure-Kinect-SDK-v1.4.1/tools/k4arecord.dll",

          ]
        },
        {
          "destination": "<(module_root_dir)/examples/electron/node_modules/electron/dist",
          "files": [
              "<(body_tracking_sdk_dir)/tools/directml.dll",
              "<(body_tracking_sdk_dir)/tools/onnxruntime.dll"
          ]
        }
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}
