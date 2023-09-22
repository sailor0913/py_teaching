# 简介
演示socket下两台电脑之间的通信

## 知识点
- 同步方式代码必须等待另一方响应后才能相互收到信息
- 异步方式代码不需要等待另一方响应就能相互收到信息

## 版本历史（强烈建议结合log学习代码）
<details>

<summary>第一版</summary>

- 建立最简单的socket通信，使得两台机器可以看到对方发送的消息
</details>

</details>

<details>

<summary>第二版</summary>

- 同步发送消息，必须等待双方都发送后才能相互接收到消息
</details>

<details>

<summary>第三版</summary>

- 异步发送消息，客户端可以向服务端发送消息，但是服务端无法向客户端发送消息
</details>

<details>

<summary>第四版</summary>

- 异步发送消息，可以双向通信
</details>

