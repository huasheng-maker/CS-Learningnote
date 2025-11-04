from PIL import Image
import os


def png_to_jpg(input_path, output_path=None, quality=95):
    """
    将PNG图片转换为JPG格式

    参数:
        input_path: 输入的PNG文件路径
        output_path: 输出的JPG文件路径(可选)
        quality: JPG质量(1-100)，默认为95
    """
    try:
        # 打开PNG图片
        img = Image.open(input_path)

        # 如果图片有透明通道，创建白色背景
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])  # 使用alpha通道作为mask
            img = background

        # 设置输出路径
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.jpg'

        # 保存为JPG
        img.convert('RGB').save(output_path, 'JPEG', quality=quality)
        print(f"转换成功: {input_path} -> {output_path}")
        return True

    except Exception as e:
        print(f"转换失败: {e}")
        return False


# 使用示例
png_to_jpg('ok聊天截图.png', 'output.jpg')