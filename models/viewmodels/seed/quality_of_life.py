class QualityOfLife:
    def __init__(
        self, hidden_block_mode: int, always_speedy_spin: bool, allow_physics_glitches: bool,
        always_peekaboo: bool, skip_quiz: bool, always_i_spy: bool, quizmo_always_appears: bool, foliage_item_hints: bool,
        hidden_panel_visibility: int, i_spy_panel_hints: int, cook_without_frying_pan: bool, shorten_cutscenes: bool, cutscene_mode: int, skip_epilogue: bool
    ):

        self.HiddenBlockMode = hidden_block_mode
        self.AlwaysSpeedySpin = always_speedy_spin
        self.PreventPhysicsGlitches = not allow_physics_glitches
        self.AlwaysPeekaboo = always_peekaboo
        self.SkipQuiz = skip_quiz
        self.AlwaysISpy = always_i_spy
        self.QuizmoAlwaysAppear = quizmo_always_appears
        self.FoliageItemHints = foliage_item_hints
        self.VisibleHiddenPanels = hidden_panel_visibility == 1
        self.ISpyPanelHints = i_spy_panel_hints
        self.CookWithoutFryingPan = cook_without_frying_pan
        self.CutsceneMode = cutscene_mode if cutscene_mode is not None else int(shorten_cutscenes)
        self.SkipEpilogue = skip_epilogue
