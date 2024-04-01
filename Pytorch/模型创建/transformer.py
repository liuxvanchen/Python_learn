import torch
from torch import nn
import math


class TransformerModel(nn.Module):
    def __init__(self, vocabulary_size, input_size, layers, heads_num, feedforward_dim, max_seq_length):
        # 初始化
        super(TransformerModel, self).__init__()
        self.embedding = nn.Embedding(vocabulary_size, input_size)
        self.pos_encoder = nn.Embedding(max_seq_length, input_size)  # 编码器
        self.transformer = nn.Transformer(d_model=input_size,
                                          nhead=heads_num,
                                          num_encoder_layers=layers,
                                          num_decoder_layers=layers,
                                          dim_feedforward=feedforward_dim)
        self.decoder = nn.Linear(input_size, vocabulary_size)  # 解码器
        self.init_weights()  # 初始化权重

    def init_weights(self):
        initrange = 0.1
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.decoder.bias.data.zero_()
        self.decoder.weight.data.uniform_(-initrange, initrange)

    def forward(self, src, tgt, src_mask, tgt_mask, src_padding_mask, tgt_padding_mask, memory_key_padding_mask):
        # 将输入的源数据序列传递给嵌入层，转换为稠密的向量表示
        src = self.embedding(src) * math.sqrt(input_size)
        # 处理目标数据序列（同上
        tgt = self.embedding(tgt) * math.sqrt(input_size)
        # 位置编码（源数据，目标数据

        # 将编码后的源序列、目标序列和四个掩码传递给Transformer模型。
        # src_mask和tgt_mask用于防止在注意力计算中将来的信息泄露给模型。
        # src_padding_mask和tgt_padding_mask用于告诉模型忽略掉那些是填充的词。
        output = self.transformer(src, tgt, src_mask, tgt_mask, None,
                                  src_padding_mask, tgt_padding_mask, memory_key_padding_mask)
        output = self.decoder(output)

        return output


# 定义一些超参数
input_size = 512  # 输入词向量的维度
num_layers = 6  # transformer堆栈中的编码器和解码器的层数
num_heads = 8  # 多头注意力机制中的头数
dim_feedforward = 2048  # 前馈网络的维度
max_seq_length = 100  # 序列的最大长度
vocab_size = 10000  # 词汇表大小

# 设置设备
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 实例化模型
model = TransformerModel(vocab_size, input_size, num_layers, num_heads, dim_feedforward, max_seq_length).to(device)

# 创建一个源序列和一个目标序列
src = torch.randint(0, vocab_size, (10, max_seq_length), dtype=torch.long).to(device)  # (batch_size, sequence_length)
tgt = torch.randint(0, vocab_size, (10, max_seq_length), dtype=torch.long).to(device)  # (batch_size, sequence_length)

# 随机数据
# 注意力和padding遮罩还没被定义，实际应用中需要定义这些遮罩来避免注意力机制关注到无关的位置。

# 将数据输入模型
output = model(src, tgt, src_mask=None, tgt_mask=None, src_padding_mask=None, tgt_padding_mask=None,
               memory_key_padding_mask=None)

print(output.shape)  # (batch_size, sequence_length, vocab_size)
