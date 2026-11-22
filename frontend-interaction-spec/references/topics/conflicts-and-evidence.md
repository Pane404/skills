# 冲突与证据（12 组冲突 + 91 条编号索引）

> 目录：一、12 组冲突台账 ｜ 二、91 条编号索引 ｜ 三、证据边界 ｜ 四、使用规则

> 5 组已裁定给单值并留覆盖痕迹；7 组保留分歧须列各方取值与证据等级，不得擅自调和。

## 一、12 组冲突台账

| # | 冲突项 | 各方取值 | 证据等级 | 裁决层 | 状态 |
|---:|---|---|---|---|---|
| <a id="c1"></a>1 | Toast / Snackbar 时长 | Android 2/3.5s vs M3 4–10s vs 项目基线 3–5s（方案 §8 第③层裁定；原库 3–7s 只读保留） vs Snackbar 4–6/6–10s | B / C | 3 项目基线 | 已裁定（方案 §8 第③层） |
| <a id="c2"></a>2 | 触控目标下限 | **合规地板**：SC 2.5.8 AA ≥24×24 CSS px 或符合 spacing / equivalent / inline / user-agent / essential 例外；**项目默认**：≥44×44、间距 ≥24px；M3 48px 为平台取值 | A / B | 3 项目基线（默认取最严，地板不可覆盖） | 已裁定（方案 §8 第③层） |
| <a id="c3"></a>3 | 纯黑 OLED | 省电 vs halation（光晕） | B / E | 4 当次任务约束 | 保留分歧（按第②层随技术栈决定） |
| <a id="c4"></a>4 | M3 是否弃用 navigation drawer | M3 Expressive 弃用 vs 其他系统仍用 | B | 2 平台约定 | 保留分歧（按第②层随技术栈决定） |
| <a id="c5"></a>5 | 菜单模态性 | Radix 菜单模态 vs W3C APG 非模态 | A / D | 1 外部基础规范 | 保留分歧（按第②层随技术栈决定） |
| <a id="c6"></a>6 | Anvil Popover `modal` 默认值 | code 页 props 表标 `true` vs design/Peek 页明文默认不困焦点 | B（同站自相矛盾） | 以官方 prose 为准 | 已裁定（方案 §8 第③层） |
| <a id="c7"></a>7 | 点遮罩关闭 | Polaris「一律不」 vs Radix「默认可」 vs iOS/Android 各异 | B / D | 按「是否含未保存数据」分型 | 保留分歧（按第②层随技术栈决定） |
| <a id="c8"></a>8 | hover 延迟 | Radix 700/300、Dialtone 300、NN/g 200–300（E 级二手转述，仅作背景，不作取值依据）、Tooltip 300–600/150 | B / C / D | 方案 §8 已裁定 300–700ms，具体随所用库，禁 0ms | 已裁定（方案 §8 第③层） |
| <a id="c9"></a>9 | Peek / HoverCard 尺寸 | ≤360×540（Anvil）vs 260–320px（HoverCard）vs peek 72–96px vs True Sheet 150px | B / D | 按语义分型，不硬统一 | 保留分歧（按第②层随技术栈决定） |
| <a id="c10"></a>10 | 感知延迟阈值 | Doherty 100–400ms / NN/g 0.1、1、10s / >2s 进度 / >10s 取消 | C / D | 保留为区间带，勿取单值 | 保留分歧（按第②层随技术栈决定） |
| <a id="c11"></a>11 | 间距口径 | 8 / 12 / 24px 多种说法 | B / D | 3 项目基线 | 已裁定（方案 §8 第③层） |
| <a id="c12"></a>12 | 点外关顶层还是底层、Esc 可否禁用 | 各家实现不同 | D | 4 当次任务约束 | 保留分歧（按第②层随技术栈决定） |

> 原库 `3–7s`、24/44/48px 等为只读旧值，本项目按第 ③ 层项目基线覆盖：Toast 3–5s、触控 ≥44×44、焦点环 2px、对比度 4.5:1 / 3:1、hover 300–700ms。

## 二、91 条编号索引

| 编号 | 证据与适用边界 | 证据等级 | 裁定或来源 |
|---|---|---|---|
| L1-01 | 来源与方法 | B/D | [按层来源](sources.md#sources-l1) |
| L1-02 | 来源与方法 | B/D | [按层来源](sources.md#sources-l1) |
| L1-03 | 来源与方法 | B/D | [按层来源](sources.md#sources-l1) |
| L1-05 | 来源与方法 | B/D | [按层来源](sources.md#sources-l1) |
| L1-07 | 来源与方法 | B/D | [按层来源](sources.md#sources-l1) |
| L1-08 | 来源与方法 | B/D | [按层来源](sources.md#sources-l1) |
| <a id="e-l10-01"></a>L10-01 | WCAG 2.4.11 AA 要求焦点组件未被完全遮挡；项目基线更严格。参见 [硬规则](../contracts/hard-rules.md)。 | B | — |
| L10-02 | 含 `aria-disabled` 与自定义键位取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-03 | 含「归还由浏览器还是手写负责」取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-04 | 含 `showModal()` 是否自动归还取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-05 | 含「表单是否禁用 Esc」取舍 | B | [裁定 c12](#c12) |
| L10-06 | 含点遮罩关闭各方取值与 `closedby` 降级 | B | [裁定 c7](#c7) |
| <a id="e-l10-07"></a>L10-07 | 文档 inert 与滚动锁分开实现；原生模态的 C6 须另核对滚动根与滚动条补偿。见 [浮层契约](../contracts/overlay-contract.md)。 | B | — |
| <a id="e-l10-08"></a>L10-08 | 原生 Dialog 靠浏览器阻断背景，自定义模态核对可达性及困焦。见 [浮层契约](../contracts/overlay-contract.md)。 | B | — |
| L10-09 | 含 `<output>` 隐式映射是否免写 ARIA 取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-10 | 含「全部移除 vs 替换瞬时」取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-11 | 含「首选等价路径」各方取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-12 | 含 2.5.1 与 2.5.7 归属划分 | B | [按层来源](sources.md#sources-l10) |
| L10-13 | 含 1.4.13 三条件与 `title` 取舍 | B | [裁定 c8](#c8) |
| L10-14 | 含七态/五态与 spinner 阈值取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-15 | 含错误提示位置与 `role="alert"` 取舍 | B | [按层来源](sources.md#sources-l10) |
| L10-16 | 含膨胀预算各方取值 | B | [按层来源](sources.md#sources-l10) |
| L10-17 | 含窗口类 3 类/5 类口径 | B | [按层来源](sources.md#sources-l10) |
| L10-18 | 含业务优先级/CSS 层叠取舍 | B | [按层来源](sources.md#sources-l10) |
| L2-04 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-09 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-10 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-11 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-15 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-16 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-17 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| L2-26 | 来源与方法 | B/D | [按层来源](sources.md#sources-l2) |
| <a id="e-l3-01"></a>L3-01 | 页内条按对象范围与动态时机区分命名、播报。见 [状态反馈](../contracts/hard-rules.md#status-feedback)。 | B | — |
| <a id="e-l3-02"></a>L3-02 | 全局状态随条件解除；显示期间保留恢复信息。状态语义见 [状态反馈](../contracts/hard-rules.md#status-feedback)。 | B | — |
| L3-03 | 含时长 2/3.5s·3–5s·3–7s（原库只读旧值，本项目按项目基线覆盖为 3–5s）·4–10s 与堆叠上限 3 / 3–4 / 3–5 各方取值、W3C | B | [裁定 c1](#c1) |
| L3-04 | 含 M2/M3 4–10s 与社区 4–6s / 6–10s 时长各方取值、Web 混称 Toast 的术语取舍 | B | [裁定 c1](#c1) |
| L3-05 | 含 Carbon 存档中心 vs Clarity 角标持久单条的消歧、到达播报各方取值 | B | [按层来源](sources.md#sources-l3) |
| L3-06 | 含 > 1s / > 150ms / > 2s 阈值分层、Eufemia `role="alert"` 与 polite 播报取舍 | B | [裁定 c10](#c10) |
| L3-07 | 含 spinner 时长上限 2–10s / < 4s / > 4s 各方取值、反对整页 `aria-busy` | B | [裁定 c10](#c10) |
| L3-08 | 含 23%/25–40%/30–40%/50% 感知提升各方取值、aidxn > 3s 换 spinner 与 1–10s 骨架的等待上限取舍 | B | [裁定 c10](#c10) |
| <a id="e-l3-09"></a>L3-09 | 成功零条和首次使用属于空状态；权限、请求失败和超时按 [错误状态](../cards/L3-10.md) 处理。 | B | — |
| <a id="e-l3-10"></a>L3-10 | 字段规则见 [字段校验](../contracts/hard-rules.md#field-validation)，区块故障按需给恢复路径，状态信息在原上下文可达。 | B | — |
| L3-11 | 含「绿色面板是否必备」取舍 | B | [按层来源](sources.md#sources-l3) |
| L3-12 | 含 role 选择分档取舍 | B | [按层来源](sources.md#sources-l3) |
| L3-13 | 含 last-write-wins 取舍 | B | [按层来源](sources.md#sources-l3) |
| <a id="e-l3-14"></a>L3-14 | 最新改动实际保存成功后再显示已保存；失败仍提供重试。播报判据见 [状态反馈](../contracts/hard-rules.md#status-feedback)。 | B | — |
| L3-15 | 含「Undo 是否算乐观 UI」取舍 | B | [按层来源](sources.md#sources-l3) |
| <a id="e-l3-16"></a>L3-16 | 提示条显示期是展示策略；撤销期限由最终提交、恢复能力决定。适用限时判据见 [WCAG 2.2.1](https://www.w3.org/TR/WCAG22/#timing-adjustable)。 | B | — |
| L3-17 | 含第 9 章时长口径取舍 | B | [裁定 c10](#c10) |
| L3-18 | 含第 9 章分带口径取舍 | B | [裁定 c10](#c10) |
| L4-01 | 含第 9 章「点遮罩关闭」冲突与取舍 | B | [裁定 c7](#c7) |
| L4-02 | 含 alert 四义消歧、第 9 章 Esc 取舍 | B | [按层来源](sources.md#sources-l4) |
| <a id="e-l4-03"></a>L4-03 | 风险和外部后果决定是否需复核、纠错或确认。法务、财务和数据场景按 [WCAG 3.3.4](https://www.w3.org/TR/WCAG22/#error-prevention-legal-financial-data)。 | B | — |
| L4-04 | 含第 9 章 trigger click/hover/focus 取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-05 | 含第 9 章「响应式铺满≠takeover」取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-06 | 含第 9 章 Anvil `modal` 默认值取舍 | B | [裁定 c6](#c6) |
| L4-07 | 含 WCAG 1.4.13 三条件、第 9 章 APG WIP 取舍 | B | [裁定 c8](#c8) |
| L4-08 | 含 peek 四义消歧、第 9 章「冲突与取舍」 | B | [裁定 c9](#c9)、[延迟 c8](#c8) |
| L4-09 | 含第 9 章 ARIA/焦点各家分歧、与 L4-08 互指 | B | [裁定 c9](#c9)、[延迟 c8](#c8) |
| L4-10 | 含双形态消歧与「冲突与取舍」 | B | [按层来源](sources.md#sources-l4) |
| L4-11 | 含与 L4-12 同族消歧、菜单模态性取舍 | B | [裁定 c5](#c5) |
| L4-12 | 含与 L4-11 同族消歧、数量阶梯取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-13 | 含指针虚拟锚点、可发现性铁律与「冲突与取舍」 | B | [按层来源](sources.md#sources-l4) |
| L4-14 | 含与 Tabs/导航消歧、W3C 与 APG tabindex 取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-15 | 含 50+ 规模判据、combobox 语义取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-16 | 含模态性判定、与 L4-17 分工 | B | [按层来源](sources.md#sources-l4) |
| L4-17 | 含 Standard/Modal 分型、断点自适应与 M2/M3 取舍 | B | [裁定 c4](#c4) |
| L4-18 | 含 peek 尺寸各方取值与手势/内滚动优先级 | B | [裁定 c9](#c9) |
| L4-19 | 含 Cancel 必需与点遮罩关闭的平台差异取舍 | B | [裁定 c7](#c7) |
| L4-20 | 含 close 焦点归还到「当前张」的取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-21 | 含步数上限与 aria-modal 各家取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-22 | 含 Pajamas 三层策略与双义取舍 | B | [按层来源](sources.md#sources-l4) |
| L4-23 | 含 15 秒规则与频控的平台差异 | B | [按层来源](sources.md#sources-l4) |
| L4-24 | 含点外关闭关顶层/底层的各方取值 | B | [裁定 c12](#c12) |
| <a id="e-l4-25"></a>L4-25 | 按原生 Dialog 和 Popover 分型选择 API，关闭配置和 C6 分别核对。见 [浮层契约](../contracts/overlay-contract.md) 与 [HTML](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element)。 | B | — |
| L5-02 | 来源与方法 | B/D | [按层来源](sources.md#sources-l5) |
| L5-04 | 来源与方法 | B/D | [按层来源](sources.md#sources-l5) |
| L5-05 | 来源与方法 | B/D | [按层来源](sources.md#sources-l5) |
| L5-07 | 来源与方法 | B/D | [按层来源](sources.md#sources-l5) |
| L5-08 | 来源与方法 | B/D | [按层来源](sources.md#sources-l5) |
| L7-01 | 来源与方法 | B/D | [按层来源](sources.md#sources-l7) |
| L7-02 | 来源与方法 | B/D | [按层来源](sources.md#sources-l7) |
| L7-03 | 来源与方法 | B/D | [按层来源](sources.md#sources-l7) |
| L7-04 | 来源与方法 | B/D | [按层来源](sources.md#sources-l7) |
| L8-01 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |
| L8-02 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |
| L8-04 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |
| L8-07 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |
| L8-10 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |
| L8-13 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |
| L8-18 | 来源与方法 | B/D | [按层来源](sources.md#sources-l8) |

## 三、证据边界

- 所有尺寸 / 时长 / 延迟数值来自规范与文档，**未做真机、读屏器、多浏览器实测**。
- L9 视觉流派一手规范较少，来源偏社区实践；NN/g、Baymard、Apple HIG 暗色原文等仅为二手转述，不得写成官方依据。
- 平台政策类具时效性，以官方页面当前措辞为准；`popover=hint`、CSS anchor positioning、`closedby` 等新特性按渐进增强标注。

## 四、使用规则

1. 按适用条目和编号查 §一。已裁定项采用对应基线并留痕；保留分歧注明条件、各方取值与证据等级。
2. 禁止把社区实践 / 转述升级为官方规范。
3. 硬约束与 5 组基线的唯一真源是 `../contracts/hard-rules.md`；本专题只记各方取值与证据。
