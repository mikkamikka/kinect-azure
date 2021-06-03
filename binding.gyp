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
        "<(module_root_dir)/sdk/sensor-sdk-1.4.1/build/native/include",
        "<(body_tracking_sdk_dir)/sdk/include",
        "<(module_root_dir)/sdk/Nuitrack/include",
        "<(module_root_dir)/sdk/Nuitrack/include/middleware",
        "<(module_root_dir)/sdk/glut/include",
        "<(module_root_dir)/sdk/freeglut/include"

      ],
      "libraries": [
        "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4a.lib",
        "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4arecord.lib",
        "<(body_tracking_sdk_dir)/sdk/windows-desktop/amd64/release/lib/k4abt.lib",
        "<(module_root_dir)/sdk/Nuitrack/lib/Win64/nuitrack.lib",
        "<(module_root_dir)/sdk/Nuitrack/lib/Win64/middleware.lib",
        "<(module_root_dir)/sdk/glut/lib/x64/glut32.lib",
        "<(module_root_dir)/sdk/freeglut/lib/x64/freeglut.lib"
      ],
      "copies": [
        {
          "destination": "<(module_root_dir)/build/Release",
          "files": [

            "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/depthengine_2_0.dll",
            "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4a.dll",
            "<(module_root_dir)/sdk/sensor-sdk-1.4.1/lib/native/amd64/release/k4arecord.dll"

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
