import os

# JSON对象
lectures = {
    "01_GPU Hardware and CUDA Development Tools": ["GPU hardware", "CUDA program development tools"],
    "02_Thread Organization in CUDA": ["Thread organization in CUDA"],
    "03_4_Basic Framework and Error Detection in CUDA Programs": ["Basic framework of CUDA programs", "Error detection in CUDA programs"],
    "05_Key to Achieving GPU Acceleration": ["Key to achieving GPU acceleration"],
    "06_8_Memory Organization and Usage in CUDA": ["Memory organization in CUDA", "Efficient use of various types of memory"],
    "09_Reasonable Use of Atomic Functions": ["Reasonable use of atomic functions"],
    "10_Basic Functions within a Warp": ["Basic functions within a warp"],
    "11_CUDA Streams": ["CUDA streams"],
    "12_Unified Memory": ["Unified memory"],
    "13_Developing a Simple Molecular Dynamics Simulation Program": ["Developing a simple molecular dynamics simulation program"],
    "14_Introduction to Several CUDA Libraries": ["Thrust", "cuBLAS", "cuSolver", "cuRAND"]
}

# 创建目录和文件并生成README.md
with open("README.md", 'w', encoding='utf-8') as readme_file:
    readme_file.write("# CUDA Programming\n\n")
    readme_file.write("This is a repository for learning CUDA programming.\n\n")
    
    for lecture_id_name, contents in lectures.items():
        lecture_id_name = lecture_id_name.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "") + ".cpp"
        # 创建目录
        os.makedirs(lecture_id_name, exist_ok=True)
        
        # 在README中添加章节标题
        readme_file.write(f"## {lecture_id_name}\n\n")
        
        for content in contents:
            # 文件名不能有空格和特殊字符，替换为下划线
            file_name = content.replace(" ", "_").replace("-", "_").replace(",", "").replace("(", "").replace(")", "") + ".cpp"
            file_path = os.path.join(lecture_id_name, file_name)
            
            # 创建文件并写入初始内容
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"// {content}\n\n")
                file.write(f'/*\nLecture: {lecture_id_name}\nContent: {content}\n*/\n\n')
            
            # 在README中添加文件链接
            readme_file.write(f"- [{content}](./{lecture_id_name}/{file_name})\n")
        
        # 添加空行以分隔不同的lecture
        readme_file.write("\n")

print("目录和文件创建完成，README.md文件已生成。")