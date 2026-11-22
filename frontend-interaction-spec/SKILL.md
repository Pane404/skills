---
name: frontend-interaction-spec
description: 用于前端组件选型与交互评审，根据业务场景、数据特征或想要的界面效果，推荐呈现方式和交互。任务涉及选择或比较反馈、浮层、表单、导航、页面状态，或需要判断键盘、焦点、关闭和读屏行为时使用；出现 alert、modal、popover、toast、peek 等术语时，先判断是否属于选型任务。典型任务：保存后如何反馈、删除前是否确认、列表与详情如何并排。纯配色、排版、文案润色及既定交互的样式调整不适用。
version: 1.2.3
agent_created: true
---

# 前端组件选型与交互行为契约

> 只做决策与评审，不产出实现代码。规则全部自包含在本包内，不引用外部路径。
> 包结构：`references/cards/` 91 张标准/简卡 · `references/index/` 6 份指针 · `references/contracts/` 4 份横切规则 · `references/topics/` 5 份长专题。

## 0 先消歧（上下文优先，不无谓追问）

先从场景、交互要求和技术栈推断术语含义；上下文足以选型时直接给结论。
只有缺失信息会改变组件或行为契约时，才问一个能区分候选方案的问题。

| 说法 | 可能语义 | 区分判据 |
|---|---|---|
| alert | 浏览器原生 / 页内 Alert / ARIA role / AlertDialog | 要打断用户，还是只提示？ |
| peek | Anvil 悬停预览 / HoverCard / 底部抽屉档位 / 链接预览 | 悬停预览、侧边抽屉，还是底部面板？ |
| popover | Popover 组件 / Popover API | 界面组件，还是浏览器 API？ |
| 弹窗 / dialog | Dialog / AlertDialog / 确认框 / 全屏 | 要不要背景停止响应？ |
| drawer / sheet | 侧边 Drawer / Side Sheet / Bottom Sheet | 从哪边出？要不要阻断背景？ |
| toast / snackbar | Toast / 含动作 Snackbar / Notification | 需要用户回看或操作吗？ |

完整对照见 `references/index/glossary.md`。

## 1 决策树

先消歧，按请求分别判断操作前防护与操作后反馈，再查候选组件和适用契约。只改配色、字体、排版、动效风格、插画或纯业务逻辑时，交给对应流程。

**业务场景入口**：先判断用户主要要查找、比较、编辑、批量处理还是追踪，再根据数据的层级、数量和状态，查阅 `references/topics/data-display-notes.md` 或 `references/topics/page-flows.md`。给出首选方案、专业术语和关键交互。批量写入或流程实际发送通知时，按 `references/topics/data-display-notes.md` 判定发送或操作结果。逐条处理后自动通知内部团队也适用。给出明确成功、明确失败、结果未知三态，结果未知先查状态或复用原幂等键，权限或收件人失败单列。只有缺失信息会改变方案时，才问一个关键问题。

```
A 操作前防护（有实质后果的动作或离开未保存流程时独立判断）
  ├ 低风险且完整可恢复 → 执行 + 可达 Undo
  ├ 不可恢复或有重大外部后果 → 操作前复核、纠错或确认，说明对象与影响
  └ 必须立即阻断并回应 → AlertDialog；轻量非阻断确认可用 Popconfirm

B 操作后反馈（按 HR-10；验证可达性后再定载体）
  ├ 结果反馈已充分、可访问且必要操作可达 → 省略额外提示
  ├ 就地状态语义不足 → 补可访问语义；需用户恢复时给常驻错误与操作
  ├ 对象级常驻 / 系统级常驻 → 页内 Alert / Banner
  ├ 瞬时轻量、可安全错过且别处可达 → Toast
  └ 结果跨页面或需回看 → Notification

C 组件与任务的关系
  ├ 锚定 · 纯文本 → Tooltip
  ├ 锚定 · 可选预览 → Peek / HoverCard；必要操作走显式入口
  ├ 锚定 · 筛选 / 列设置 / 多控件 → Popover（可含输入框，立即生效）
  ├ 需提交 / 保护数据 / 多步 → 超一屏或需 URL 则页面，否则 Dialog
  └ 需并排对照 → 非模态并排面板 / 布局；必须阻断背景才用模态 Drawer / Sheet
```

## 2 克制与硬规则

- 优先就地反馈和清楚的主操作，轻量结果保持非阻断。危险操作先过 A，保存结果按 B 判断。
- 共享规则见 `references/contracts/hard-rules.md`。依任务的合规目标执行 Floor（含适用的状态消息语义），在允许范围内使用项目默认与库约定。适用的浮层行为按组件契约核对，动效和表达细节按场景选择。
- 输出先用白话给首选方案，再给专业术语与可执行行为、适用条件；替代、必检与规范编号按题目需要展开，不输出全套清单，高后果场景命中时才展开作用范围与后果。
  信息不足时只问一个会改变方案的问题；信息充分时直接给方案。条件会改变答案时给条件方案；只展开与本题直接相关的分支，不把其他题型的检查项带进来。

## 3 高频速查（直达规则与卡片）

| 说法 | 路径 |
|---|---|
| 保存成功 / 操作成功 | `references/contracts/hard-rules.md#status-feedback` |
| 页内对象级提示（贴字段/区块） | `references/cards/L3-01.md` |
| 系统级通告（贴整页/跨路由） | `references/cards/L3-02.md` |
| 异步通知 / 通知中心 | `references/cards/L3-05.md` |
| 表单校验失败 / 字段报错 | `references/contracts/hard-rules.md#field-validation` |
| 区块请求失败 | `references/cards/L3-10.md` |
| 空结果 / 无数据 | `references/cards/L3-09.md` |
| 加载中 / 骨架屏 | `references/cards/L3-08.md` |
| 断网 / 离线 | `references/cards/L3-13.md` |
| 弹窗 / 模态 / modal | `references/cards/L4-01.md` |
| 紧急阻断 / 安全确认 | `references/cards/L4-02.md` |
| 删除确认 / 二次确认 | `references/cards/L4-03.md` |
| 气泡确认 / popconfirm | `references/cards/L4-04.md` |
| popover / 列设置 / 筛选 | `references/cards/L4-06.md` |
| tooltip / 悬停说明 | `references/cards/L4-07.md` |
| peek / hover 预览 | `references/cards/L4-08.md` |
| hovercard | `references/cards/L4-09.md` |
| 下拉菜单 | `references/cards/L4-11.md` |
| 命令面板 / ⌘K | `references/cards/L4-15.md` |
| 抽屉 / drawer | `references/cards/L4-16.md` |
| 侧边面板 / side sheet | `references/cards/L4-17.md` |
| 底部面板 / bottom sheet | `references/cards/L4-18.md` |
| 图片放大 / lightbox | `references/cards/L4-20.md` |
| 原生 popover API / showModal | `references/cards/L4-25.md` |
| 视频 / 音频播放器、树形表格 / 甘特图 | `references/topics/data-display-notes.md` |
| 批量操作栏、聊天 / 会话界面 | `references/topics/page-flows.md` |
| 焦点管理 / 键盘 | `references/cards/L10-01.md`、`references/cards/L10-02.md` |
| 焦点困住 | `references/cards/L10-03.md` |
| Esc 关闭 | `references/cards/L10-05.md` |
| 背景 inert | `references/cards/L10-08.md` |

## 4 六个意图族

| 族 | 场景 | 入口 |
|---|---|---|
| 反馈提示 | 保存成功 / 报错 / 空结果 / 加载 | `references/index/intents.md` |
| 浮层弹窗 | 该弹窗吗 / 弹哪一种 / peek 是什么 | `references/index/intents.md` |
| 表单输入 | 校验时机 / 选择器 / 日期 / 上传 | `references/index/intents.md` |
| 导航结构 | 分页还是无限滚动 / 状态进 URL | `references/index/intents.md` |
| 页面流程 | 多步表单 / 结算 / 空结果 / 错误页 | `references/topics/page-flows.md` |
| 行为契约 | 焦点 / 键盘 / Esc / inert / 状态 | `references/contracts/overlay-contract.md` |

并列入口上限 2 个；契约面为条件必读，不计入额度。

## 5 高频场景映射

| 用户说法 | 第一动作 |
|---|---|
| 「加个弹窗」 | 用上下文判断是否必须打断；会改变方案且信息不足时提问 |
| 「保存成功提示一下」 | 按 B 与 HR-10 判断反馈是否充分、可访问及需不需要额外载体 |
| 「删除要确认吗」 | 按 A 检查风险、恢复范围和外部后果，再单独确定结果反馈 |
| 「加个 peek」 | 按 §0 从上下文确定预览或面板类型 |
| 「列设置 / 筛选」 | Popover（就地、即时生效、不提交） |
| 「hover 显示说明」 | 纯文本 → Tooltip；含可选动作 → Peek / HoverCard（必须操作走显式按钮） |
| 「移动端底部菜单」 | Bottom Sheet / Action Sheet |
| 「表单校验失败」 | 字段级按表单契约；提交或整个区块请求失败时走对应错误态 |
| 「表格太宽看不全」 | 冻结列 / 横向滚动；要并排对照 → Drawer |
| 「填一半退出」 | 保护未保存数据 → Dialog 或路由守卫 |

## 6 契约触发（条件必读，不占入口额度）

只要涉及以下任一，必须读 `references/contracts/overlay-contract.md`：

- 模态 / 非模态判定
- 焦点移入、困住、归还
- Esc / 点外关闭
- 背景 inert / 锁滚动
- 表单未保存数据保护

涉及数值冲突时读 `references/topics/conflicts-and-evidence.md`。
涉及合规、默认值覆盖及 `HR-xx` 细则时，读 `references/contracts/hard-rules.md`。字段错误直接读 `references/contracts/hard-rules.md#field-validation`。

## 7 输出前检查表

- [ ] 结论解决了用户的场景；仅在能帮助决策时给替代项。
- [ ] 核对适用的状态语义、操作前防护、焦点、键盘、关闭与读屏。需要解释方案依据或辅助验收时，再在答复中列出相关 HR 或 C 编号。
- [ ] 对照 `references/contracts/anti-patterns.md` 的适用条目；按需核对冲突台账及证据。
- [ ] 保持选型与评审范围，出处可追溯。

## 8 按需加载与 fallback

| 需要 | 读 |
|---|---|
| 全部条目 | `references/index/entries.md` |
| 高频速查 | `references/index/hot.md` |
| 按意图找 | `references/index/intents.md` |
| 按分面找 | `references/index/facets.md` |
| 按说法找 | `references/index/aliases.md` |
| 术语消歧 | `references/index/glossary.md` |
| 反模式 | `references/contracts/anti-patterns.md` |
| 冲突谁覆盖谁 | `references/contracts/precedence.md` |
| 风格 / 页面 / 数据展示 | `references/topics/visual-styles.md`、`references/topics/page-flows.md`、`references/topics/data-display-notes.md` |
| 出处 | `references/topics/sources.md` |

fallback：速查未命中时查六族入口。缺失信息会改变选型时问一个关键问题；已有充分上下文时直接给出判断，必要时说明覆盖边界。多个 Skill 同时适用时只负责组件与交互决策。

## 9 冲突处理

按命中的条目和台账编号读 `references/contracts/precedence.md`。已裁定项采用对应基线并留痕；未裁定项说明分歧、适用环境和证据等级。用户偏好与适用标准冲突时给满足标准的最小替代。二手资料注明来源层级。
