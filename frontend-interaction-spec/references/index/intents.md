# 意图族入口（6 族 → 场景 → 路径）

> 目录：一、反馈提示 ｜ 二、浮层弹窗 ｜ 三、表单输入 ｜ 四、导航结构 ｜ 五、页面流程 ｜ 六、行为契约
> 并列入口上限 2 个；契约面为条件必读，不计入额度。

## 一、反馈提示

| 场景 | 路径 |
|---|---|
| 就地结果的反馈与可达性 | `../contracts/hard-rules.md#status-feedback` |
| 瞬时轻量结果 | `../cards/L3-03.md` |
| 对象级常驻（贴字段/区块） | `../cards/L3-01.md` |
| 持续状态 / 系统级 | `../cards/L3-02.md` |
| 异步可回看 | `../cards/L3-05.md` |
| 字段级错误 | `../contracts/hard-rules.md#field-validation` |
| 区块请求失败 | `../cards/L3-10.md` |
| 整页连接中断 / 同步状态 | `../cards/L3-02.md`、`../cards/L3-13.md` |
| 空结果 / 首次使用 | `../cards/L3-09.md` |

## 二、浮层弹窗

| 场景 | 路径 |
|---|---|
| 不回应无法安全继续 | `../cards/L4-02.md`、`../cards/L4-03.md` |
| 就地调整、即时生效、不提交（列设置 / 筛选） | `../cards/L4-06.md` |
| 纯文本短说明 | `../cards/L4-07.md` |
| 悬停预览且别处可达 | `../cards/L4-08.md`、`../cards/L4-09.md` |
| 需与列表 / 图表并排对照 | `../cards/L4-16.md`、`../cards/L4-18.md` |
| 超一屏或需 URL | 页面或路由（见 `../topics/page-flows.md`） |
| 多义词先消歧 | `../index/glossary.md` |

## 三、表单输入

| 场景 | 路径 |
|---|---|
| 校验时机与错误呈现 | `../contracts/hard-rules.md#field-validation` |
| 精确数值 vs 相对手感 | `../cards/L2-04.md` |
| 值可自由输 vs 受限长列表 | `../cards/L2-09.md`、`../cards/L2-10.md` |
| 少量比较 vs 中量固定值 | `../cards/L2-11.md`、`../cards/L2-16.md` |
| 立即生效 vs 提交后生效 | `../cards/L2-17.md`、`../cards/L2-15.md` |
| 长且高风险表单 | `../cards/L8-13.md` |

## 四、导航结构

| 场景 | 路径 |
|---|---|
| 先数目的地再选导航 | `../cards/L5-02.md`、`../cards/L5-04.md` |
| 同处换面 vs 换参数 | `../cards/L5-05.md`、`../cards/L1-08.md` |
| 来找 vs 随便逛 | `../cards/L5-07.md`、`../cards/L5-08.md` |
| 单值低风险就地改 | `../cards/L7-03.md` |

## 五、页面流程

| 场景 | 路径 |
|---|---|
| 落地页 / 定价页 | `../cards/L8-01.md`、`../cards/L8-02.md` |
| 首次使用引导 | `../cards/L8-04.md` |
| 结果收窄 / 详情 | `../cards/L8-07.md`、`../cards/L8-10.md` |
| 多步表单 | `../cards/L8-13.md` |
| 页面模式全表 | `../topics/page-flows.md` |

## 六、行为契约（条件必读）

| 场景 | 路径 |
|---|---|
| 模态 / 焦点 / 键盘 / Esc / inert | `../contracts/overlay-contract.md` |
| 焦点可见与不被遮挡 | `../contracts/hard-rules.md` |
| 拖放替代 | `../cards/L10-11.md` |
| 一致帮助、冗余输入 | `../contracts/hard-rules.md`（SC 3.2.6 / 3.3.7） |
| 错误恢复 | `../cards/L10-15.md` |
| 撤销重做 | `../cards/L3-16.md` |
