const path = require('path');

module.exports = () => {
  const KINECT_SENSOR_SDK_URL = 'https://www.nuget.org/api/v2/package/Microsoft.Azure.Kinect.Sensor/1.4.0';
  const KINECT_BODY_TRACKING_SDK_URL = 'https://www.nuget.org/api/v2/package/Microsoft.Azure.Kinect.BodyTracking/1.0.1';
  const KINECT_BODY_TRACKING_DEPENDENCIES_URL = 'https://www.nuget.org/api/v2/package/Microsoft.Azure.Kinect.BodyTracking.Dependencies/0.9.1';
  const KINECT_CUDNN_URL = 'https://www.nuget.org/api/v2/package/Microsoft.Azure.Kinect.BodyTracking.Dependencies.cuDNN/0.9.1';

  const TARGET_SDK_DIR = path.resolve(__dirname, '../sdk');
  const TARGET_KINECT_SENSOR_SDK_ZIP = path.resolve(TARGET_SDK_DIR, 'sensor-sdk-1.4.0.zip');
  const TARGET_KINECT_BODY_TRACKING_SDK_ZIP = path.resolve(TARGET_SDK_DIR, 'body-tracking-sdk-1.0.1.zip');
  const TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_ZIP = path.resolve(TARGET_SDK_DIR, 'body-tracking-dependencies.zip');
  const TARGET_KINECT_CUDNN_ZIP = path.resolve(TARGET_SDK_DIR, 'cudnn.zip');

  const TARGET_KINECT_SENSOR_SDK_DIR = path.resolve(TARGET_SDK_DIR, 'sensor-sdk-1.4.0');
    // const TARGET_KINECT_BODY_TRACKING_SDK_DIR = path.resolve(TARGET_SDK_DIR, 'body-tracking-sdk-1.0.1');
    const TARGET_KINECT_BODY_TRACKING_SDK_DIR = path.resolve(TARGET_SDK_DIR, 'Azure-Kinect-Body-Tracking-SDK-1.1.0');

//   const TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_DIR = path.resolve(TARGET_SDK_DIR, 'body-tracking-dependencies');
  const TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_DIR = path.resolve(TARGET_SDK_DIR, 'Azure-Kinect-Body-Tracking-SDK-1.1.0');

//   const TARGET_KINECT_CUDNN_DIR = path.resolve(TARGET_SDK_DIR, 'cudnn');
  const TARGET_KINECT_CUDNN_DIR = path.resolve(TARGET_SDK_DIR, 'Azure-Kinect-Body-Tracking-SDK-1.1.0');


  const appRootDlls = {
    // 'onnxruntime.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'lib/native/amd64/release/onnxruntime.dll'),
    // 'dnn_model_2_0.onnx': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'content/dnn_model_2_0.onnx'),
    // 'cublas64_100.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_DIR, 'lib/native/amd64/release/cublas64_100.dll'),
    // 'cudart64_100.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_DIR, 'lib/native/amd64/release/cudart64_100.dll'),
    // 'vcomp140.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_DIR, 'lib/native/amd64/release/vcomp140.dll'),
    // 'cudnn64_7.dll': path.resolve(TARGET_KINECT_CUDNN_DIR, 'lib/native/amd64/release/cudnn64_7.dll'),

    'cublas64_11.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cublas64_11.dll'),
    'cublasLt64_11.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cublasLt64_11.dll'),
    'cudart64_110.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cudart64_110.dll'),
    'cudnn_cnn_infer64_8.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cudnn_cnn_infer64_8.dll'),
    'cudnn_ops_infer64_8.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cudnn_ops_infer64_8.dll'),
    'cudnn64_8.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cudnn64_8.dll'),
    'cufft64_10.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/cufft64_10.dll'),
    'directml.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/directml.dll'),
    'dnn_model_2_0_lite_op11.onnx': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/dnn_model_2_0_lite_op11.onnx'),
    'dnn_model_2_0_op11.onnx': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/dnn_model_2_0_op11.onnx'),
    'myelin64_1.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/myelin64_1.dll'),
    'nvinfer.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/nvinfer.dll'),
    'nvinfer_plugin.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/nvinfer_plugin.dll'),
    'nvrtc64_111_0.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/nvrtc64_111_0.dll'),
    'nvrtc-builtins64_111.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/nvrtc-builtins64_111.dll'),
    'onnxruntime.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/onnxruntime.dll'),
    'onnxruntime_providers_shared.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/onnxruntime_providers_shared.dll'),
    'onnxruntime_providers_tensorrt.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/onnxruntime_providers_tensorrt.dll'),
    'vcomp140.dll': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/vcomp140.dll')
    // '': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/'),
    // '': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/'),
    // '': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/'),
    // '': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/'),
    // '': path.resolve(TARGET_KINECT_BODY_TRACKING_SDK_DIR, 'tools/'),


  };

  return {
    KINECT_SENSOR_SDK_URL,
    KINECT_BODY_TRACKING_SDK_URL,
    KINECT_BODY_TRACKING_DEPENDENCIES_URL,
    KINECT_CUDNN_URL,
    TARGET_SDK_DIR,
    TARGET_KINECT_SENSOR_SDK_ZIP,
    TARGET_KINECT_BODY_TRACKING_SDK_ZIP,
    TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_ZIP,
    TARGET_KINECT_CUDNN_ZIP,
    TARGET_KINECT_SENSOR_SDK_DIR,
    TARGET_KINECT_BODY_TRACKING_SDK_DIR,
    TARGET_KINECT_BODY_TRACKING_DEPENDENCIES_DIR,
    TARGET_KINECT_CUDNN_DIR,
    appRootDlls
  }
};