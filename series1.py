import numpy as np

# 定义文件路径（注意处理路径中的空格）
file_path = r"D:\PRO sense\softsensing_data\time-series-1\X_test.npy"

try:
    # 加载.npy文件
    data = np.load(file_path)
    
    # 打印基本信息
    print("="*50)
    print(f"文件路径: {file_path}")
    print(f"数组形状: {data.shape}")  # 显示维度信息，如(样本数, 时间步, 特征数)
    print(f"数据类型: {data.dtype}")  # 显示数据类型，如float32
    
    # 根据维度智能显示内容
    if data.ndim == 1:
        print("\n前20个数据值:")
        print(data[:20])
    elif data.ndim == 2:
        print("\n前3行前10列数据:")
        print(data[:3, :10])
    elif data.ndim == 3:
        print("\n第一个样本的前3时间步前5特征:")
        print(data[0, :3, :5])
    else:
        print("\n数据内容（前100个元素）:")
        print(data.flatten()[:100])
    
    # 数值统计信息（如果是数值型数据）
    if np.issubdtype(data.dtype, np.number):
        print("\n统计摘要:")
        print(f"最小值: {np.min(data):.4f}")
        print(f"最大值: {np.max(data):.4f}")
        print(f"平均值: {np.mean(data):.4f}")
        print(f"标准差: {np.std(data):.4f}")

except FileNotFoundError:
    print(f"错误：文件未找到，请检查路径是否正确\n{file_path}")
except Exception as e:
    print(f"加载文件时出错: {str(e)}")