# AI Coding 工程实践档案

> 会写固件的 Agent 工程师 · 能碰硬件的 Vibe Coder

## 📖 在线查看

**🌐 [GitHub Pages 在线展示](https://ly-1157799217.github.io/ai-coding-engineering-portfolio/)**（推荐）

一页式精美展示，包含：
- 两个项目的 12 项核心工程指标
- 3 个典型调试案例（含数据对比）
- 人在环多 Agent 协同工作流
- 外部复核 6 轮收敛记录

## 📂 仓库内容

本仓库整理两个项目的工程指标、调试案例与 AI 协同方法，展示 AI Coding / AI Agent 应用开发中的实际工程实践成果。

### 目录结构

```
ai-coding-engineering-portfolio/
├── index.html                          # 一页式展示入口
├── data/                               # 详细证据文档
│   ├── projects-metrics.md             # 两个项目的工程指标
│   ├── case-01-circuit-breaker.md      # TCP 熔断器自愈案例
│   ├── case-02-heap-fragmentation.md   # 堆碎片化 + Git 锚点案例
│   ├── case-03-upload-atomicity.md     # 上传非原子性修复案例
│   ├── multi-agent-workflow.md         # 人在环多 Agent 协同流程
│   └── external-audit-log.md           # 外部复核 6 轮记录
└── README.md                           # 本文件
```

### 文档导航

| 文档 | 内容 |
|------|------|
| [两个项目的工程指标](data/projects-metrics.md) | ESP32 固件 / 树莓派 Hub 的量化指标与指标定义 |
| [案例 1：TCP 熔断器](data/case-01-circuit-breaker.md) | 单向闩锁 → 三态熔断器；人工设计的三段反证测试；12/12 次自愈 |
| [案例 2：堆碎片化 + Git 锚点](data/case-02-heap-fragmentation.md) | 坏基线上三次优化零效果 → 回锚点后逐一击破；4 条预注册判据 |
| [案例 3：上传非原子性](data/case-03-upload-atomicity.md) | 中断即毁旧数据 → 三阶段替换 + 开机恢复；能力边界与实测方法 |
| [人在环多 Agent 协同流程](data/multi-agent-workflow.md) | 角色分工、人机边界、AI 失误与提炼出的判据 |
| [外部复核 6 轮记录](data/external-audit-log.md) | 18→9→7→4→4→2，累计 44 条缺陷、零误报，含自查清单 9 条 |

## 🔗 相关项目

- [ESP32 桌面智能显示终端](https://github.com/LY-1157799217/Visual-desktop-TV-decoration) · [Gitee 镜像](https://gitee.com/LY115LY/Visual-desktop-TV-decoration)
- [树莓派 MQTT 智能中控](https://github.com/LY-1157799217/mqtt-edge-hub) · [Gitee 镜像](https://gitee.com/LY115LY/mqtt-edge-hub)

## 📊 核心数据摘要

### ESP32（含无Pi版、Pi Hub版）固件设计
- 12 小时零重启运行（731 心跳 / 0 崩溃）
- 熔断器自动恢复 12/12 次（2.8h 真实环境）→ [📹 查看完整演示视频](https://www.bilibili.com/video/BV1UDh169E3s)
- 堆内存零泄漏（+2,632 B 净增长）
- 首页加载优化 55%（5.2s → 2.33s）
- 并发请求 42/42 成功（修复前第 2 发即 RST）

### 树莓派 Hub 设计
- 4 服务 26 秒开机就绪
- 端-边-云三层失效边界设计
- 60s 幂等缓存 + 45s 结果未知语义
- Pi 不可达时直连兜底成功率 100%
- 企微多机器人零串扰拓扑

## 🛠️ 技术栈

**嵌入式**：ESP32-C3 (Arduino)、ST7789 TFT、AsyncTCP、SPIFFS  
**边缘计算**：树莓派 5、Python 3、Flask、MQTT、systemd  
**多 Agent 协同**：Claude Code(主力)、OpenClaw、WorkBuddy、Codex (GPT)  
**人机协同机制**：人机分工边界、预注册判据、外部复核、失败模式归档  
**工具链**：Git(锚点管理)、串口/HTTP 双通道取证

---

📌 **本档案展示的是实际工程实践中的量化数据与方法论，所有数据均可在源代码与日志中验证。**
