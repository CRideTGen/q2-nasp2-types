#   Copyright 2022 Chase Ridenour
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import importlib

from qiime2.plugin import Plugin

from q2_nasp2_types import __version__

plugin = Plugin(name='nasp2_types',
                version=__version__,
                package='q2_nasp2_types',
                website='https://github.com/CRideTGen/q2-readmappers')



importlib.import_module("q2_nasp2_types.alignment._transformers")
