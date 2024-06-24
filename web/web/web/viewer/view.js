import * as GaussianSplats3D from '@mkkellogg/gaussian-splats-3d';

// 封装函数，接受文件路径作为参数，并返回一个 Promise
export function setupViewer(file) {
    return new Promise((resolve, reject) => {
        // 创建 Viewer 实例
        const viewer = new GaussianSplats3D.Viewer({
            'cameraUp': [0, -1, -0.6],
            'initialCameraPosition': [-1, -4, 6],
            'initialCameraLookAt': [0, 4, 0],
            'sharedMemoryForWorkers': false,
            'gpuAcceleratedSort': false
        });

        // 添加 Splat 场景
        viewer.addSplatScene(file, {
            'splatAlphaRemovalThreshold': 100,
            'showLoadingSpinner': true,
            'position': [0, 1, 0],
            'rotation': [0, 0, 0, 1],
            'scale': [1.5, 1.5, 1.5]
        })
        .then(() => {
            // 启动 Viewer
            viewer.start();
            resolve(viewer); // 解析 Promise 并传递 Viewer 实例
        })
        .catch(error => {
            reject(error); // 如果发生错误，拒绝 Promise 并传递错误信息
        });
    });
}



