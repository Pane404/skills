# 来源登记（只记出处，不作运行时读取配置）

> 目录：一、标准与规范 ｜ 二、Agent 与设计方法 ｜ 三、设计系统 ｜ 四、工具与规范 ｜ 五、按层来源归属 ｜ 六、引用与更新规则 ｜ 七、二手转述处理 ｜ 八、证据等级

## 一、标准与规范

| 来源 | 用途 | 等级 |
|---|---|---|
| W3C WCAG 2.2 — https://www.w3.org/TR/WCAG22/ | 2.4.7 / 2.4.11 / 2.5.7 / 2.5.8 / 3.2.6 / 3.3.7 等硬约束 | A |
| WAI-ARIA Authoring Practices — https://www.w3.org/WAI/ARIA/apg/ | 键盘交互与角色模式 | A |
| ARIA in HTML — https://www.w3.org/TR/html-aria/ | 原生元素的隐式角色 | A |
| MDN Web Docs — https://developer.mozilla.org/ | Popover API / dialog / inert / `closedby` | A |
| WHATWG HTML — https://html.spec.whatwg.org/multipage/interactive-elements.html#the-dialog-element | Dialog 模态、聚焦与关闭 | A |
| W3C WAI — https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html | 适用状态消息与辅助技术通知 | A |
| W3C WAI — https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html | 预录同步字幕 SC 1.2.2 | A |
| W3C WAI — https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html | 预录音频描述 SC 1.2.5 | A |
| WCAG 2.1 — https://www.w3.org/TR/WCAG21/ | 1.4.3 / 1.4.11 对比度 | A |
| ISO 9241-110 — 交互原则 | 一致性与可预期性 | A |

## 二、Agent 与设计方法

| 来源 | 用途 | 等级 |
|---|---|---|
| Anthropic — Equipping agents for the real world with Agent Skills | 渐进式披露三级加载 | A |
| Anthropic Agent Skills 文档 | frontmatter 与打包规范 | A |
| NN/g — Progressive Disclosure — https://www.nngroup.com/articles/progressive-disclosure/ | 披露层级与并列入口 | C |
| GitLab Pajamas — Choosing a messaging pattern | 消息模式决策表 | B |
| ServiceTitan Anvil — Peek pattern | Peek 语义与「不承载独家信息」 | B |
| Feature-Sliced Design — https://feature-sliced.design/ | 多轴定位 | B |
| Diátaxis — https://diataxis.fr/ | 按需求形态组织文档 | C |
| C4 model — https://c4model.com/ | 分层受众与下钻 | C |
| Brad Frost — Atomic Web Design | 构成层级与「心智模型非目录规范」 | C |
| Panda CSS — Cascade Layers | 级联优先级 | B |
| Baymard Institute — 结算与表单可用性研究 | 结算流程与表单摩擦 | E |

## 三、设计系统

| 来源 | 用途 | 等级 |
|---|---|---|
| Material Design 3 | 组件与时长口径 | B |
| Apple Human Interface Guidelines | 触控与平台约定 | B |
| Adobe Spectrum（含 Design Data 结构词汇） | 结构角色与级联 | B |
| Ant Design | 组件实现与默认值 | D |
| Carbon Design System | 数据表格与密度 | B |
| Shopify Polaris | 文案与 guarded closing | B |
| Radix UI Primitives | 浮层实现与默认模态性 | D |
| GOV.UK Design System | 表单与错误摘要模式 | B |

## 四、工具与规范

| 来源 | 用途 | 等级 |
|---|---|---|
| skill-creator（三级加载、frontmatter、quick_validate、package_skill） | Skill 结构规范 | A |
| darwin-skill（8 维 rubric、test-prompts、棘轮、dry_run） | 优化循环 | B |

## 五、按层来源归属

| 层 | 主要来源 |
|---|---|
| L0 设计令牌 | WCAG 对比度、M3 / HIG 尺寸与字阶 |
| <a id="sources-l1"></a>L1 动作与基础控件 | APG 按钮/链接模式、原生 HTML 语义 |
| <a id="sources-l2"></a>L2 输入与选择 | APG 组合框/列表箱、Carbon 表单规范 |
| <a id="sources-l3"></a>L3 反馈与系统状态 | M3 Snackbar、Polaris 文案、NN/g 状态可见性 |
| <a id="sources-l4"></a>L4 浮层与弹窗 | MDN Popover/dialog、Anvil Peek、Radix、Polaris |
| <a id="sources-l5"></a>L5 导航与信息结构 | M3 导航、NN/g 信息架构、HIG 标签栏 |
| L6 数据展示 | Carbon / AntD 表格、数据可视化通则 |
| <a id="sources-l7"></a>L7 渐进披露与容器 | NN/g 披露、APG 手风琴/标签页 |
| <a id="sources-l8"></a>L8 页面级与流程模式 | Polaris 流程、Baymard 结算研究 |
| L9 视觉流派 | 社区风格库与 CSS 实践为主（一手偏少） |
| <a id="sources-l10"></a>L10 交互与行为契约 | WCAG 2.2、APG、MDN inert / focus 管理 |

## 六、引用与更新规则

1. 卡片与契约引用来源时只写等级与来源名，不复制检索记录与各家叫法。
2. 新增来源先登记本文件，再在条目里引用；不得先写结论后补来源。
3. 平台政策类来源具时效性，以官方页面当前措辞为准；登记时写**具体页面**与检索日期（`YYYY-MM-DD`），只写门类或站点首页不算完成登记。
4. 同一结论有多个来源时取等级最高者；等级相同取更近期的官方文档。
5. 本文件只记出处，**不作运行时读取配置**；包内不回工作区取原文。
6. `../topics/data-display-notes.md` 与 `../topics/page-flows.md` 的「工程常见但原库未覆盖」小节属**外部补充**，判据据 MDN / APG / 主流设计系统整理（等级 B/D），不冒充原库结论。
7. 每条来源登记时注明检索日期；超过 12 个月的平台政策类来源须复核页面当前措辞。
8. 同一来源的不同版本（如 WCAG 2.1 / 2.2）分别登记，不合并。
9. 删除来源前先确认没有卡片或契约仍在引用。
10. 来源变更不改变已有规则结论，只更新出处与证据等级。

## 七、二手转述处理

| 情况 | 处理 |
|---|---|
| NN/g 具体数值经第三方转述 | 标 E 级，仅作背景，不作取值依据 |
| Baymard 结算研究未读到原文 | 标 E 级，结论写成「有研究指出」而非「官方规定」 |
| Apple HIG 暗色原文未获取 | 标 E 级，不写成 HIG 强制要求 |
| Ant Design compact 数值 | 标 D 级实现文档，不作为跨平台基线 |
| 社区风格库的风格定义 | 标 E 级，仅作风格族参考 |

> 证据等级用于标注来源可靠性，不用于给结论打分；同一结论以最高等级来源为准。

## 八、证据等级

| 等级 | 含义 |
|---|---|
| A | 标准 / 官方一手 |
| B | 设计系统官方文档 |
| C | 研究机构 / 方法论 |
| D | 组件库实现文档 |
| E | 社区实践 / 二手转述（不得升级为官方依据） |
